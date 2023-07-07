from typing import Dict

from zoo.backends.base import ModelCard
from zoo.constant import Task, Backend


class ClipModelCard(ModelCard):
    model_name = "cn_clip"
    task = Task.FeatureExtraction
    backend = Backend.PYTORCH

    def available_models_detail(self) -> Dict:
        return {
            'RN50': {'param': '', 'url': ''},
            'ViT-B-16': {'param': '', 'url': ''},
            'ViT-L-14': {'param': '', 'url': ''},
            'ViT-L-14-336': {'param': '', 'url': ''},
            'ViT-H-14': {'param': '', 'url': ''},
        }

    def default_model(self) -> str:
        return 'RN50'
