from typing import Type, List
import importlib
import inspect


def subclasses_py(module_name, parent_class: Type) -> List:
    """
    获取 py 文件模块中的所有 parent_class 子类列表

    Args:
        module_name: 模块名
        parent_class: 父类

    Returns:

    """
    sub_classes = []
    module = importlib.import_module(module_name)
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj) and issubclass(obj, parent_class) and obj != parent_class:
            sub_classes.append(obj)
    return sub_classes

