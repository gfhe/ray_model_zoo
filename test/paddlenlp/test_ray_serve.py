import unittest
from pathlib import Path
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)
# -*- coding: UTF-8 -*- 
import json
import requests

from zoo import run


class PaddleNLPServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handle = run(task='SentimentAnalysis', 
                         backend='paddlenlp', 
                         model='bilstm', 
                         route_prefix='/senta',
                         name='senta')

    def test_senta(self):
        response = requests.post("http://localhost:8000/senta", json=json.dumps(['这家餐厅太棒了，很好吃！']))
        result = json.loads(response.text)
        assert result[0]['label'] == 'positive'
        

if __name__ == '__main__':
    unittest.main()
