import unittest
from pathlib import Path
import os
import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.backends.huggingface import HuggingfaceAutoModel, HuggingfacePipelineModel
from zoo.backends.registry import HUGGINGFACE

class HuggingfaceModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")

    def test_classification(self):
        model = HuggingfacePipelineModel('text-classification',HUGGINGFACE, 'roberta-large-mnli')
        ret = model("A soccer game with multiple males playing. Some men are playing a sport.")
        assert ret[0]['label'] == 'ENTAILMENT'
        return
    
    def test_distilbert_en(self):
        model = HuggingfacePipelineModel('sentiment-analysis', HUGGINGFACE, 'distilbert-base-uncased-finetuned-sst-2-english')
        ret = model("A soccer game with multiple males playing")
        assert ret[0]['label'] == 'POSITIVE'
        return
    
    def test_helsinki_en_zh(self):
        model = HuggingfaceAutoModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-en-zh')
        ret = model("My name is Wolfgang, and I live in Berlin.")
        print(ret)
    #     return
    
    def test_helsinki_zh_en(self):
        model = HuggingfaceAutoModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-zh-en')
        ret = model("我叫沃尔夫冈，我住在柏林。")
        print(ret)
        return

    def test_helsinki_de_en(self):
        model = HuggingfacePipelineModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-de-en')
        ret = model("Schön dich kennenzulernen, mein Name ist Wolfgang.")
        print(ret)
        return

if __name__ == '__main__':
    unittest.main()
