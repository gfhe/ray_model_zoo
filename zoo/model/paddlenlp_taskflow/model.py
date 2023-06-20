from pathlib import Path
import logging

from paddlenlp.taskflow import Taskflow

from zoo.config import model_dir
from zoo.model.base import Model

logger = logging.getLogger(__name__)

class PaddleNLPTaskflowModel(Model):
    """
    封装PaddleNLP模型

    模型：PaddleNLP
    用途：中文情感分析
    github：https://github.com/PaddlePaddle/PaddleNLP
    """

    def model_path(self) -> str:
        return Path(model_dir) / self.model_name

    def available_models(self) -> list:
        return ["bilstm"]

    def model_load_name(self) -> str:
        return self.model_param

    def __init__(self, model, param):
        super().__init__(model, param)
        self.model = Taskflow('sentiment_analysis', model=model, task_path=param)
        logger.info(f"PaddleNLP model deployed with model {model}")

    def forward(self, texts: list):
        """
        分析文本的情感倾向
        :param texts: 文本数据, list
        :return: 结果, List[Dict]
        """
        return self.model(texts)
