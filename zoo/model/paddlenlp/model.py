import logging

from paddlenlp.taskflow import Taskflow

from zoo.model.base import Model


logger = logging.getLogger(__name__)

class PaddleNLPModel(Model):
    """
    封装PaddleNLP模型

    模型: PaddleNLP
    用途：中文情感分析
    github: https://github.com/PaddlePaddle/PaddleNLP
    """
    def __init__(self, task, backend, model, **kwargs):
        super().__init__(task, backend, model)
        self.model = Taskflow(task=task, model=model, task_path=self.model_path, **kwargs)
        logger.info(f"PaddleNLP taskflow deployed")

    def __call__(self, texts: list):
        """
        分析文本的情感倾向
        :param texts: 文本数据, list
        :return: 结果, List[Dict]
        """
        return self.model(texts)
