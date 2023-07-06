from abc import ABC, abstractmethod
from typing import List
from zoo.constant import Task


class FeatureExtraction(ABC):
    task = Task.FeatureExtraction


class TextFeatureExtraction(FeatureExtraction):

    @abstractmethod
    def text_features(self, texts: List[str]):
        raise NotImplementedError


class ImageFeatureExtraction(FeatureExtraction):

    @abstractmethod
    def image_features(self, images: List[bytes]):
        raise NotImplementedError
