from pathlib import Path
import os
import logging

import numpy as np
from paddleocr import PaddleOCR

from zoo.model.base import Model
from zoo.model.registry import PADDLE_OCR

logger = logging.getLogger(__name__)

class PaddleOCRModel(Model):
    """
    封装PaddleOCR模型

    模型: PaddleOCR
    用途: 图片OCR
    github: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/README_ch.md
    """
    def __init__(self, model_name):
        super().__init__(task="OCR", model_lib=PADDLE_OCR, model_name=model_name)
        self.model = PaddleOCR(ocr_version=model_name, 
                               det_model_dir=os.path.join(self.model_path, 'det'), 
                               rec_model_dir=os.path.join(self.model_path, 'rec'), 
                               cls_model_dir=os.path.join(self.model_path, 'cls'))
        logger.info(f"PaddleOCR model deployed.")

    def __call__(self, image):
        """
        识别图片中的文字
        Args:
            image (bytes): 以二进制方式读取的图片
        Returns:
            result (List): OCR识别的结果 
        """
        return self.model.ocr(image)
