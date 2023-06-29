import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.backends.huggingface import HuggingfaceModel
from zoo.backends.registry import HUGGINGFACE

class HuggingfaceModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.model = HuggingfaceModel('text-classification',HUGGINGFACE, 'roberta-large-mnli')

    def test_classification(self):
        ret = self.model("A soccer game with multiple males playing. Some men are playing a sport.")
        print(ret)


if __name__ == '__main__':
    unittest.main()
