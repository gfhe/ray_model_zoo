from pathlib import Path

from config import model_dir

import torch

CN_CLIP = "cn_clip"

models = {
    CN_CLIP: {
        'RN50': {'param': '', 'url': ''},
        'ViT-B-16': {'param': '', 'url': ''},
        'ViT-L-14': {'param': '', 'url': ''},
        'ViT-L-14-336': {'param': '', 'url': ''},
        'ViT-H-14': {'param': '', 'url': ''},
    },
}


def cn_clip_models():
    """
    clip 模型支持的不同参数级别的模型
    """
    from cn_clip.clip import available_models
    return available_models()


class Model:
    def __init__(self, model_name, model_param=None):
        self.model_name = model_name
        self.model_param = model_param
        # 模型存储地址
        self.model_dir = self.get_model_dir()

        # 模型使用的硬件
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"model_dir={self.model_dir}, device={self.device}")

    def available_models(self):
        self.model_params(self.model_name)

    def get_model_dir(self) -> str:
        assert self.model_name in models
        if self.model_param is None:
            self.model_param = self.model_default_param()
        return Path(model_dir) / self.model_name / self.model_param

    def model_default_param(self) -> str:
        assert self.model_name in models
        model_param_list = self.model_params()
        return model_param_list[0]

    def model_params(self) -> list:
        return [p for p, _ in models.get(self.model_name).items()]
