from abc import ABC, abstractmethod

from zoo.constant import Task

class OCR(ABC):
    """
    OCR  任务
    """

    task = Task.OCR

    @abstractmethod
    def detect(self, image: bytes):
        """
        图片专为文字

        :param image: 输入的图片二进制数据
        """
        raise NotImplementedError
