from typing import Union, List
from transformers import pipeline

from zoo.backends.base import Model
from zoo.backends.huggingface.roberta_language_detection.model_card import RobertaModelCard
from zoo.task.language_detection import LanguageDetection


class RobertaLanguageDetect(Model, LanguageDetection):

    @property
    def device(self):
        return 'cpu'

    def __init__(self, detail_model_choice: str = None, **kwargs):
        super().__init__(RobertaModelCard(), detail_model_choice, **kwargs)
        self.model = pipeline(task='text-classification', model=self.model_path)

    def __call__(self, text: Union[List[str], str]):
        """
        TODO: 写清楚注释
        Args:
            text:

        Returns:

        """
        return self.model(text)
