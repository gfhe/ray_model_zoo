from typing import List

import cn_clip.clip as clip
import torch
from PIL import Image
from cn_clip.clip import load_from_name

from zoo.backends.base import Model
from zoo.backends.pytorch.cn_clip.model_card import ClipModelCard
from zoo.task.feature_extraction import TextFeatureExtraction, ImageFeatureExtraction


class ClipModel(Model, TextFeatureExtraction, ImageFeatureExtraction):
    """
    封装 CN Clip 模型

    模型：Chinese clip
    用途：图像
    github：https://github.com/OFA-Sys/Chinese-CLIP
    """

    @property
    def device(self):
        return "cuda" if torch.cuda.is_available() else 'cpu'

    def __init__(self, detail_model_choice: str = None, **kwargs):
        super().__init__(ClipModelCard(), detail_model_choice, **kwargs)
        self.model, self.preprocess = load_from_name(self.detail_model_choice,
                                                     device=self.device,
                                                     download_root=self.model_path)

    def text_features(self, texts: List[str]):
        """
        将文本编码为向量
        :param texts: 文本数据, list
        :return: 向量表示
        """
        tokens = clip.tokenize(list(texts)).to(self.device)
        return self.model.encode_text(tokens)

    def image_features(self, images: List[bytes]):
        """
        将图片编码为向量
        :param images: 图片二进制数据, list
        ：return: 向量表示
        """
        import io
        res = []
        for image_bytes in images:
            image = io.BytesIO(image_bytes)
            image = self.preprocess(Image.open(image)).unsqueeze(0).to(self.device)
            embedding = self.model.encode_image(image)
            res.append(embedding)
        return torch.cat(res, dim=0)
