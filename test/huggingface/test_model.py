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

    def test_classification(self):
        model = HuggingfaceModel('text-classification',HUGGINGFACE, 'roberta-large-mnli')
        ret = model("A soccer game with multiple males playing. Some men are playing a sport.")
        assert ret[0]['label'] == 'ENTAILMENT'
        return
    
    def test_distilbert_en(self):
        model = HuggingfaceModel('sentiment-analysis', HUGGINGFACE, 'distilbert-base-uncased-finetuned-sst-2-english')
        ret = model("A soccer game with multiple males playing")
        assert ret[0]['label'] == 'POSITIVE'
        return


if __name__ == '__main__':
    unittest.main()
