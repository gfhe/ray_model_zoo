import logging

from transformers import pipeline

from zoo.backends.base import Model
from zoo.backends.registry import HUGGINGFACE

logger = logging.getLogger(__name__)

class HuggingfaceModel(Model):
    """
    封装Huggingface模型

    github: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/README_ch.md
    """

    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        super().__init__(task=task, backend=backend, model=model)
        self.instance = pipeline(task=task, 
                                 model=self.model_path,
                                 **kwargs)
        logger.info(f"Huggingface model deployed.")

    def __call__(self, sentence):
        """
        调用模型
        Args:
            sentence (str): 要进行推理的文本
        Returns:
            result (List): 模型推理结果
        """
        return self.instance(sentence)
