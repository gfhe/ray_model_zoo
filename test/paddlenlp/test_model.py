import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)

from zoo.model.paddlenlp import PaddleNLPModel


class ModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.model = PaddleNLPModel('sentiment_analysis', 'paddlenlp', 'bilstm')

    def test_senta(self):
        ret = self.model('这家餐厅太棒了，很好吃！')
        assert ret[0]['label'] == 'positive'


if __name__ == '__main__':

    unittest.main()
