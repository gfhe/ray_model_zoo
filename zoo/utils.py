from typing import Union, Dict

from ray import serve
from zoo.model.registry import registry
from zoo.model.utils import get_serve_class


def run(task: str, backend: str, model:str, autoscaling_config: Union[Dict, None]=None, **kwargs):
    # 校验指定模型是否合法
    if not task in registry:
        raise ValueError(f"Task '{task}' not available, should be in {list(registry.keys())}.")
    if not backend in registry[task]:
        raise ValueError(f"Backend '{backend}' not avaliable for task '{task}', \
                            should be in {list(registry[task].keys())}.")
    if not model in registry[task][backend]['models']:
        raise ValueError(f"Model '{model}' not availabel for task '{task}' and model '{model}', \
                            should be in {list(registry[task][backend]['models'].keys())}.")

    # 校验是否提供了指定模型所需的额外参数
    backend_config = registry[task][backend]
    model_config = backend_config['models'][model]
    for p in model_config['param']:
        if p not in kwargs:
            raise ValueError(f"Model '{model}' requires parameter '{p}', which is not provided.")

    # 获取Serve部署类
    serve_name = model_config.get('serve', registry[task][backend]['default_serve'])
    serve_class = get_serve_class(serve_name)

    # 在特定backend下进行task名称转换
    task = backend_config.get('task_alias', task)

    # 部署Serve实例
    handle = serve.run(serve_class.bind(task=task, model=model, **kwargs))
    return handle