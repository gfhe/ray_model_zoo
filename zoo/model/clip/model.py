from pathlib import Path

import cn_clip.clip as clip
import torch
from PIL import Image
from cn_clip.clip import load_from_name, available_models

from zoo.config import model_dir
from zoo.model.base import Model, CN_CLIP


class ClipModel(Model):
    """
    封装 CN Clip 模型

    模型：Chinese clip
    用途：图像
    github：https://github.com/OFA-Sys/Chinese-CLIP
    """

    def model_path(self) -> str:
        return Path(model_dir) / self.model_name
        # TODO: online deploy
        # return "/home/ray/tiny_clip/model"

    def available_models(self) -> list:
        return available_models()

    def model_load_name(self) -> str:
        return self.model_param

    def default_model_param_name(self) -> str:
        return "RN50"

    def __init__(self):
        super().__init__(CN_CLIP)
        self.model, self.preprocess = load_from_name(self.model_load_name(),
                                                     device=self.device,
                                                     download_root=self.model_path())

    def encode_image(self, images_bytes: list):
        """
        将图片编码为向量
        :param images_bytes: 图片二进制数据, list
        ：return: 向量表示
        """
        import io
        res = []
        for image_bytes in images_bytes:
            image = io.BytesIO(image_bytes)
            image = self.preprocess(Image.open(image)).unsqueeze(0).to(self.device)
            embedding = self.model.encode_image(image)
            res.append(embedding)
        return torch.cat(res, dim=0)

    def encode_text(self, texts: list):
        """
        将文本编码为向量
        :param texts: 文本数据, list
        :return: 向量表示
        """
        tokens = clip.tokenize(list(texts)).to(self.device)
        return self.model.encode_text(tokens)
