import unittest
from pathlib import Path
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)
# -*- coding: UTF-8 -*- 
import json
import requests

import ray
from ray import serve

from zoo.config import data_dir
from zoo.model.paddleocr import PaddleOCRServe


class PaddleOCRServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handle = serve.run(PaddleOCRServe.bind())

    def test_senta(self):
        response = requests.post("http://localhost:8000/ocr", json=json.dumps('https://p3.itc.cn/images01/20230621/cfd5746105d044e5bb2d973493c453ae.png'))
        result = json.loads(response.text)
        assert result[0]['label'] == 'positive'
        


if __name__ == '__main__':
    unittest.main()
