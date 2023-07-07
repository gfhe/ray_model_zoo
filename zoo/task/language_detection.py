from abc import ABC, abstractmethod
from zoo.constant import Task


class LanguageDetection(ABC):
    """
    语种识别任务
    """

    task = Task.LanguageDetection

    @abstractmethod
    def __call__(self, text):
        """
        分析文本的语种，返回符合IOS标准的缩写

        :param text: 输入的待分析文本
        """
        raise NotImplementedError
