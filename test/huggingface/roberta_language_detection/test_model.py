import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.backends.huggingface.roberta_language_detection.model import RobertaLanguageDetect


def test_papluca_xlm_roberta_base_language_detection():
    model = RobertaLanguageDetect()
    ret = model(["Jactos do exército matam 38 militantes em ataques aéreos no Noroeste do Paquistão"])
    print(ret)
    assert ret[0]['label'] == 'pt'
