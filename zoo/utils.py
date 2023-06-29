from typing import Union, Dict
import importlib

from ray import serve

from zoo.backends.registry import registry


default_autoscaling_config = {"min_replicas": 1,
                              "initial_replicas": 1,
                              "max_replicas": 2,
                              "target_num_ongoing_requests_per_replica": 5,
                              "upscale_delay_s": 10,
                              "downscale_delay_s": 10}
default_ray_actor_options={"num_cpus": 1.0, "num_gpus": 0.0}

def run(task: str,
        backend: str,
        model: str=None,
        deployment_config: Union[Dict, None]=None,
        name: str=None,
        autoscaling_config: Union[Dict, None]=None,
        ray_actor_options: Union[Dict, None]=None,
        **kwargs):
    """部署模型的入口
    
    Args:
        task (str): 要部署的任务类型
        backend (str): 要使用的后端
        model (str): 要使用的模型
        deployment_config (Dict): serve部署的配置, 若未提供则使用默认参数
        name (str): serve部署的名称
        autoscaling_config (Dict): serve部署的自动扩缩容配置, 若未提供则使用默认参数
        ray_actor_options (Dict): serve部署中actor的资源配置, 若未提供则使用默认参数
        **kwargs: 其它提供给模型的参数
    
    Returns:
        handle: serve部署的handle
    
    Raises:
        ValueError: 当提供的参数不合法时
        KeyError: 当route_prefix参数未提供时
        TypeError: 当route_prefix类型不为str时
    """

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

    # 若name未指定，则使用随机名称
    if name is None:
        name = f"{backend}:{rand_str()}"

    # 校验autoscaling_config是否合法
    if autoscaling_config is None:
        autoscaling_config = default_autoscaling_config
    
    # 校验ray_actor_options是否合法
    if ray_actor_options is None:
        ray_actor_options = default_ray_actor_options

    # 获取Serve部署类
    serve_name = model_config.get('serve', registry[task][backend]['default_serve'])
    backend_module = importlib.import_module(f"zoo.backends.{backend}")
    serve_class = getattr(backend_module, serve_name)
    serve_class = serve.deployment(autoscaling_config=autoscaling_config,
                                   ray_actor_options=ray_actor_options
                                   )(serve_class) 

    # 在特定backend下进行task名称转换
    task = backend_config.get('task_alias', task)

    # 部署Serve实例
    handle = serve.run(serve_class.bind(task=task, model=model, **kwargs), route_prefix=route_prefix, name=name)
    return handle

def rand_str():
    import random
    import hashlib
    val = random.randbytes(500)
    hash_value = hashlib.md5(val)
    return hash_value.hexdigest()[:6]
