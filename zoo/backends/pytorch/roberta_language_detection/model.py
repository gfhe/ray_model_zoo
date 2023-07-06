from zoo.task.language_detection import LanguageDetection
from zoo.backends.base import Model, ModelCard
from zoo.backends.pytorch.roberta_language_detection.model_card import RobertaModelCard


class RobertaLanguageDetect(Model, LanguageDetection):
    @property
    def device(self):
        return 'cpu'

    @classmethod
    def model_card(cls) -> ModelCard:
        return RobertaModelCard()

    def __init__(self, detail_model_choice: str = None, **kwargs):
        super().__init__(detail_model_choice, **kwargs)
        self.model = ******

    def lang(self, text: str):
        pass
