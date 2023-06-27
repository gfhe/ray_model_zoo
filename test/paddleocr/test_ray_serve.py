# -*- coding: UTF-8 -*- 
import unittest
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)

import json
import requests

from zoo import run
from zoo.model.registry import PADDLE_OCR


class PaddleOCRServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handle = run(task='OCR', 
                         backend=PADDLE_OCR)

    def test_ocr(self):
        with open('data/news1.png', 'rb') as f:
            img_bytes = f.read()
        response = requests.post("http://localhost:8000/ocr", data=img_bytes)
        result = json.loads(response.text)
        import pprint
        pprint.pprint(result)
        assert len(result[0]) == 30
        


if __name__ == '__main__':
    unittest.main()
