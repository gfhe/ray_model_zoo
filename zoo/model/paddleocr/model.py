from pathlib import Path
import os
import logging

import numpy as np
from paddleocr import PaddleOCR

from zoo.config import model_dir
from zoo.model.base import Model

logger = logging.getLogger(__name__)

class PaddleOCRModel(Model):
    """
    封装PaddleOCR模型

    模型：PaddleOCR
    用途：图片OCR
    github：https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/README_ch.md
    """

    def model_path(self) -> str:
        return Path(model_dir) / self.model_name

    def available_models(self) -> list:
        return ["PP-OCRv3"]

    def model_load_name(self) -> str:
        return self.model_param

    def __init__(self, model, param):
        super().__init__(model, param)
        self.model = PaddleOCR(det_model_dir=os.path.join(param, 'det'), 
                               rec_model_dir=os.path.join(param, 'rec'), 
                               cls_model_dir=os.path.join(param, 'cls'))
        logger.info(f"PaddleOCR model deployed with model {model}")

    def forward(self, image):
        """
        分析文本的情感倾向
        :param texts: 文本数据, List
        :return: 结果, List[Dict]
        """
        return self.model.ocr(image)
