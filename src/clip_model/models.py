import os
import torch

ROOT_DIR=os.getenv("RAY_MODEL_ZOO", "/workspace/ray_model_zoo")
MODEL_CN_CLIP=ROOT_DIR+"/cn_clip"

class Model:
    def __init__(self) -> None:
        self.model_dir=os.getenv(MODEL_CN_CLIP, '../../model/cn_clip')
        self.device = "cuda" if torch.cuda.is_available() else "cpu"