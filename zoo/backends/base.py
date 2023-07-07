import json
import logging
from abc import ABC, abstractmethod
from typing import Dict, List

from zoo.config import model_dir
from zoo.constant import Backend, Task

logger = logging.getLogger(__name__)


class Requirement:
    """
    NOTE: 没有检查依赖冲突的机制
    """

    def __init__(self):
        self.deps = {}

    def include(self, requirements: List):
        for requirement in requirements:
            self.deps.update(requirement.all_dependencies())
        return self

    def add_dependency(self, dependencies: Dict[str, str]):
        self.deps.update(dependencies)
        return self

    def all_dependencies(self):
        return self.deps


class ModelCard(ABC):
    """
    模型静态信息
    """

    @property
    @abstractmethod
    def model_name(self) -> str:
        """
        定义模型的名字
        """
        pass

    @property
    @abstractmethod
    def task(self) -> Task:
        """
        定义模型完成的任务
        """
        pass

    @property
    @abstractmethod
    def backend(self) -> Backend:
        """
        定义模型完成的backend
        """
        pass

    @abstractmethod
    def available_models_detail(self) -> Dict:
        """
        不同参数级别的模型，key为模型的名字
        """
        raise NotImplementedError

    def available_models(self):
        return [name for name in self.available_models_detail()]

    def valid_detail_model_choice(self, detail_model_choice: str) -> bool:
        return detail_model_choice in self.available_models_detail()

    @abstractmethod
    def default_model(self) -> str:
        raise NotImplementedError

    def info(self) -> Dict:
        return {
            "name": self.model_name,
            "default_model": self.default_model(),
            "task": self.task.value,
            "backend": self.backend.value,
            "models": self.available_models_detail()
        }

    def simple_info(self) -> Dict:
        return {
            "name": self.model_name,
            "default_model": self.default_model(),
            "task": self.task.value,
            "backend": self.backend.value,
        }

    def __str__(self):
        return json.dumps(self.simple_info())


class Model(ABC):
    """
    模型的抽象类
    """

    @property
    @abstractmethod
    def device(self):
        """
        设备名
        """
        pass

    def __init__(self, model_card: ModelCard, detail_model_choice: str = None, **kwargs):
        """
        :param detail_model_choice:具体的模型规模的名字
        """
        self.model_card = model_card
        self.detail_model_choice = self.model_card.default_model() if detail_model_choice is None \
            else detail_model_choice

        self.kwargs = kwargs
        self.model_path = self.get_model_path()

        # 模型使用的硬件（框架相关，需要在子类中确定）
        logger.info(f"Using model={self.model_card}, "
                    f"model_choice={self.detail_model_choice}, "
                    f"model_path={self.model_path}, ")

    def get_model_path(self) -> str:
        """
        模型存储路径（,相对于model 文件夹）

        :ref:`zoo.config.model_dir`
        """
        return model_dir / self.model_card.backend.value / self.model_card.model_name / self.detail_model_choice


class Serve(ABC):
    from fastapi import FastAPI
    app = FastAPI()

    @abstractmethod
    def health(self):
        """
        暴露服务健康的endpoint, 每个serve 自己实现。
        """
        raise NotImplementedError
