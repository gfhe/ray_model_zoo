from typing import Dict

from zoo.backends.base import ModelCard
from zoo.constant import Task, Backend


class RobertaModelCard(ModelCard):
    model_name = "roberta-language-detection"
    task = Task.LanguageDetection
    backend = Backend.HUGGINGFACE
    available_models = {'papluca-xlm-roberta-base': {'param': '', 'url': ''}}

    def available_models_detail(self) -> Dict:
        return self.available_models

    def default_model(self) -> str:
        return next(iter(self.available_models))
