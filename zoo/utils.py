from typing import Union, Dict
import importlib

from ray import serve

from zoo.backends.registry import registry


def run(task: str, backend: str, model:str=None, deployment_config: Union[Dict, None]=None, **kwargs):
    # 校验指定任务和后端是否合法
    if not task in registry:
        raise ValueError(f"Task '{task}' not available, should be in {list(registry.keys())}.")
    if not backend in registry[task]:
        raise ValueError(f"Backend '{backend}' not avaliable for task '{task}', \
                            should be in {list(registry[task].keys())}.")

    # 校验是否提供了指定模型所需的额外参数
    backend_config = registry[task][backend]
    if model is None:
        model = next(iter(backend_config['models']))
    if not model in registry[task][backend]['models']:
        raise ValueError(f"Model '{model}' not availabel for task '{task}' and model '{model}', \
                            should be in {list(registry[task][backend]['models'].keys())}.")
    model_config = backend_config['models'][model]
    for p in model_config['param']:
        if p not in kwargs:
            raise ValueError(f"Model '{model}' requires parameter '{p}', which is not provided.")

    # 校验Serve部署相关参数
    if 'route_prefix' not in deployment_config:
        raise KeyError(f"'route_prefix' not provided in deployment_config.")
    route_prefix = deployment_config['route_prefix']
    if not isinstance(route_prefix, str):
        raise TypeError(f"'route_prefix' should be a string starts with '/', got {type(route_prefix)} object.")
    if not route_prefix.startswith('/'):
        raise ValueError(f"'route_prefix' should be a string starts with '/', got {route_prefix}")

    # 获取Serve部署类
    serve_name = model_config.get('serve', registry[task][backend]['default_serve'])
    backend_module = importlib.import_module(f"zoo.backends.{backend}")
    serve_class = getattr(backend_module, serve_name)
    serve_class = serve.deployment(autoscaling_config={
                                        "min_replicas": 1,
                                        "initial_replicas": 1,
                                        "max_replicas": 2,
                                        "target_num_ongoing_requests_per_replica": 5,
                                        "upscale_delay_s": 10,
                                        "downscale_delay_s": 10
                                   },
                                   ray_actor_options={"num_cpus": 1.0, "num_gpus": 0.0}
                                   )(serve_class) 

    # 在特定backend下进行task名称转换
    task = backend_config.get('task_alias', task)

    # 部署Serve实例
    handle = serve.run(serve_class.bind(task=task, model=model, **kwargs), route_prefix=route_prefix)
    return handle