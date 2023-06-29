import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.backends.paddleocr import PaddleOCRModel
from zoo.backends.registry import PADDLE_OCR

class PaddleOCRModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.model = PaddleOCRModel('OCR', PADDLE_OCR, 'PP-OCRv3')

    def test_ocr(self):
        with open('data/news1.png', 'rb') as f:
            img_bytes = f.read()
        ret = self.model(image=img_bytes)
        print(ret)
        assert len(ret[0]) == 30


if __name__ == '__main__':
    unittest.main()
