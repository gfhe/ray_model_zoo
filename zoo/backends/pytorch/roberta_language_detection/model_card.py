from zoo.backends.base import ModelCard
from typing import Dict
from zoo.constant import Task, Backend


class RobertaModelCard(ModelCard):
    model_name = "roberta-language_detection"
    task = Task.LanguageDetection
    backend = Backend.PYTORCH

    def available_models_detail(self) -> Dict:
        return {
            'papluca--xlm-roberta-base-language-detection': {'param': '', 'url': ''},
        }

    def default_model(self) -> str:
        return 'papluca--xlm-roberta-base-language-detection'

