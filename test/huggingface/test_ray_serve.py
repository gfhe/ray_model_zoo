# -*- coding: UTF-8 -*- 
import unittest
import sys
sys.path.append('D:\Workspace\model_zoo')
print(sys.path)

import json
import requests

from zoo import run
from zoo.backends.registry import HUGGINGFACE

class HuggingfaceServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handle = run(task='NaturalLanguageInference', 
                         backend=HUGGINGFACE, 
                         deployment_config={'route_prefix': "/nli"})

    def test_ocr(self):
        response = requests.post("http://localhost:8000/nli", json=json.dumps(["A soccer game with multiple males playing. Some men are playing a sport."]))
        result = json.loads(response.text)
        assert result[0]['label'] == 'ENTAILMENT'
        


if __name__ == '__main__':
    unittest.main()
