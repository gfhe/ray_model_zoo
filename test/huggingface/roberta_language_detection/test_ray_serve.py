# -*- coding: UTF-8 -*- 
import sys
sys.path.append('D:\Workspace\model_zoo')

import json
import requests

from zoo import run
from zoo.constant import Backend
    
def test_papluca_xlm_roberta_base_language_detection():
    handle = run('LanguageDetection', Backend.HUGGINGFACE, 'roberta-language-detection', 
                    route_prefix='/lang-det', 
                    name='lang-det')
    response = requests.post("http://localhost:8000/lang-det", json=json.dumps(["Jactos do exército matam 38 militantes em ataques aéreos no Noroeste do Paquistão"]))
    result = json.loads(response.text)
    assert result[0]['label'] == 'pt'
    return
