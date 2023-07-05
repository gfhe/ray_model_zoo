# -*- coding: UTF-8 -*- 
import sys
sys.path.append('D:\Workspace\model_zoo')

import json
import requests

from zoo import run
from zoo.backends.registry import HUGGINGFACE


def test_classification():
    handle = run('NaturalLanguageInference', HUGGINGFACE, 'roberta-large-mnli', route_prefix='/nli', name='nli')
    response = requests.post("http://localhost:8000/nli", json=json.dumps(["A soccer game with multiple males playing. Some men are playing a sport."]))
    result = json.loads(response.text)
    assert result[0]['label'] == 'ENTAILMENT'

def test_distilbert_en():
    handle = run('SentimentAnalysis', HUGGINGFACE, 'distilbert-base-uncased-finetuned-sst-2-english', 
                    route_prefix='/senta', 
                    name='senta')
    response = requests.post("http://localhost:8000/senta", json=json.dumps(["A soccer game with multiple males playing"]))
    result = json.loads(response.text)
    assert result[0]['label'] == 'POSITIVE'
    return

def test_helsinki_en_zh():
    handle = run('Translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-en-zh', 
                    route_prefix='/trans_ez', 
                    name='en_zh')
    response = requests.post("http://localhost:8000/trans_ez", json=json.dumps("My name is Wolfgang, and I live in Berlin."))
    result = json.loads(response.text)
    assert result == '我叫沃尔夫冈 我住在柏林</s>'
    return

def test_helsinki_zh_en():
    handle = run('Translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-zh-en', 
                    route_prefix='/trans_ze', 
                    name='zh_en')
    response = requests.post("http://localhost:8000/trans_ze", json=json.dumps("我叫沃尔夫冈，我住在柏林。"))
    result = json.loads(response.text)
    assert result == 'My name is Wolfgang, and I live in Berlin.</s>'
    return
    
def test_papluca_xlm_roberta_base_language_detection():
    handle = run('LanguageDetection', HUGGINGFACE, 'papluca--xlm-roberta-base-language-detection', 
                    route_prefix='/lang-det', 
                    name='lang-det')
    response = requests.post("http://localhost:8000/lang-det", json=json.dumps(["Jactos do exército matam 38 militantes em ataques aéreos no Noroeste do Paquistão"]))
    result = json.loads(response.text)
    assert result[0]['label'] == 'pt'
    return
