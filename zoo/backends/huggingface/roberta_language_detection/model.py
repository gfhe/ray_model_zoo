from typing import Union, List

from transformers import pipeline

from zoo.task.language_detection import LanguageDetection
from zoo.backends.base import Model, ModelCard
from zoo.backends.huggingface.roberta_language_detection.model_card import RobertaModelCard


class RobertaLanguageDetect(Model, LanguageDetection):
    @property
    def device(self):
        return 'cpu'

    @classmethod
    def get_model_card(cls) -> ModelCard:
        return RobertaModelCard()

    def __init__(self, detail_model_choice: str = None, **kwargs):
        super().__init__(detail_model_choice, **kwargs)
        self.model = pipeline(task='text-classification', model=self.model_path)

    def __call__(self, text: Union[List[str], str]):
        return self.model(text)
