from typing import List

from zoo.backends.base import Model, ModelCard
from zoo.backends.pytorch.huggingface_pipeline import HuggingfacePipelineModel
from zoo.backends.pytorch.roberta_language_detection.model_card import RobertaModelCard
from zoo.constant import Task
from zoo.task.language_detection import LanguageDetection


class RobertaLanguageDetect(Model, LanguageDetection):

    @property
    def device(self):
        return 'cpu'

    def __init__(self, detail_model_choice: str = None, **kwargs):
        super().__init__(RobertaModelCard(), detail_model_choice, **kwargs)
        self.model = HuggingfacePipelineModel(task=self.model_card.task,
                                              task_alias=Task.LanguageDetection.value,
                                              model=self.detail_model_choice)

    def lang(self, texts: List[str]):
        return self.model(texts)
