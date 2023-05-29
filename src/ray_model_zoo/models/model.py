from pathlib import Path

from ray_model_zoo.config import model_dir

import torch


CN_CLIP = "cn_clip"

models = (
    CN_CLIP,
)

def get_model(model_name) -> str:
    return Path(model_dir) / model_name


def model_params(model_name):
    if CN_CLIP == model_name:
        return cn_clip_models()
    return None


def cn_clip_models():
    """
    clip 模型支持的不同参数级别的模型
    """
    from cn_clip.clip import available_models
    return available_models()


class Model:
    def __init__(self, model_name):
        self.model_name = model_name
        # 模型存储地址
        self.model_dir = get_model(model_name)

        # 模型使用的硬件
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def available_models(self):
        model_params(self.model_name)
