import logging
from typing import Any

from zoo.backends.base import Model
from zoo.backends.registry import HUGGINGFACE

logger = logging.getLogger(__name__)


class HuggingfacePipelineModel(Model):
    """
    封装Huggingface模型
    """

    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        from transformers import pipeline
        super().__init__(task=task, backend=backend, model=model)
        self.instance = pipeline(task=task,
                                 model=self.model_path,
                                 **kwargs)
        logger.info(f"Huggingface pipeline model deployed.")

    def __call__(self, sentence):
        """
        调用模型
        Args:
            sentence (str): 要进行推理的文本
        Returns:
            result (List): 模型推理结果
        """
        return self.instance(sentence)
