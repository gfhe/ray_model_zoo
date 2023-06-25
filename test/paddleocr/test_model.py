import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.model.paddleocr import PaddleOCRModel


class PaddleOCRModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.model = PaddleOCRModel('PP-OCRv3')

    def test_senta(self):
        ret = self.model('https://p3.itc.cn/images01/20230621/cfd5746105d044e5bb2d973493c453ae.png')
        assert len(ret[0]) == 30


if __name__ == '__main__':
    unittest.main()
