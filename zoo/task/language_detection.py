from abc import ABC, abstractmethod
from zoo.constant import Task
from typing import List


class LanguageDetection(ABC):
    """
    语种识别任务
    """

    task = Task.LanguageDetection

    @abstractmethod
    def lang(self, texts: List[str]):
        """
        分析文本的语种，返回符合IOS标准的缩写

        :param texts: 输入的待分析文本
        """
        raise NotImplementedError
