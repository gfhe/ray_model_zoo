import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)

from zoo.model.paddlenlp import PaddleNLPModel
from zoo.config import data_dir


# 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

class ModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.model = PaddleNLPModel('sentiment_analysis', 'paddlenlp', 'bilstm')

    def test_senta(self):
        ret = self.model('这家餐厅太棒了，很好吃！')
        print(ret)


if __name__ == '__main__':

    unittest.main()
