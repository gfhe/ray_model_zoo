import os
import logging

from paddleocr import PaddleOCR

from zoo.backends.base import Model
from zoo.backends.registry import PADDLE_OCR

logger = logging.getLogger(__name__)

class PaddleOCRModel(Model):
    """
    封装PaddleOCR模型

    模型: PaddleOCR
    用途: 图片OCR
    github: https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/README_ch.md
    """

    def __init__(self, task, backend=PADDLE_OCR, model=None, **kwargs):
        super().__init__(task=task, backend=backend, model=model)
        self.instance = PaddleOCR(ocr_version=self.model, 
                                  det_model_dir=os.path.join(self.model_path, 'det'), 
                                  rec_model_dir=os.path.join(self.model_path, 'rec'), 
                                  cls_model_dir=os.path.join(self.model_path, 'cls'), 
                                  **kwargs)
        logger.info(f"PaddleOCR model deployed.")

    def __call__(self, image):
        """
        识别图片中的文字
        Args:
            image (bytes): 以二进制方式读取的图片
        Returns:
            result (List): OCR识别的结果 
        """
        return self.instance.ocr(image)
