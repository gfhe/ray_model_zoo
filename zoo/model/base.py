from abc import ABC, abstractmethod
import logging
from pathlib import Path

from zoo.config import MODEL_DIR
from zoo.model.registry import registry

logger = logging.getLogger(__name__)


class Model(ABC):
    def __init__(self, task, backend, model):
        self.task = task
        self.backend = backend
        self.model = model
        self.model_path = self.get_model_path()

        # 模型使用的硬件（框架相关，需要在子类中确定）
        logger.info(f"Using task={self.task}, "
                    f"backend={self.backend}, "
                    f"model={self.model}, "
                    f"model_path={self.model_path}, ")

    def get_model_path(self) -> str:
        """
        模型存储路径（,相对于model 文件夹）

        :ref:`zoo.config.model_dir`
        """
        return Path(MODEL_DIR) / self.backend / self.model

    def available_models(self) -> list:
        """
        模型的不同参数级别名字列表
        """
        return [p for p, _ in registry.get(self.task).get(self.backend).get('models').items()]

    def default_model(self) -> str:
        """
        默认的模型名字：模型参数列表的第一个
        """

        assert self.model in registry[self.task][self.backend]['models']
        model_list = self.available_models()
        return model_list[0]

class Serve(ABC):
    @abstractmethod
    def health(self):
        """
        暴露服务健康的endpoint, 每个serve 自己实现。
        """
        raise NotImplementedError
