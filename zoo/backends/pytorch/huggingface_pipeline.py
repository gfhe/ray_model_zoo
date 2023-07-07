import logging
from abc import ABC

from zoo.backends.base import Model
from zoo.constant import Task

logger = logging.getLogger(__name__)


class HuggingfacePipelineModel(ABC, Model):
    """
    封装Huggingface模型
    """

    def __init__(self, task: Task = None, task_alias: str = None, detail_model_choice: str = None, **kwargs):
        from transformers import pipeline
        super().__init__(detail_model_choice, kwargs=kwargs)
        self.task = task
        self.task_alais = task_alias
        self.instance = pipeline(task=self.task_alais,
                                 model=self.model_path,
                                 **kwargs)
        logger.info(f"Huggingface pipeline model started.")

    # TODO: 可以改成list的吗？
    def __call__(self, sentence):
        """
        调用模型
        Args:
            sentence (str): 要进行推理的文本
        Returns:
            result (List): 模型推理结果
        """
        return self.instance(sentence)
