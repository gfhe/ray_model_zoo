import sys
sys.path.append('D:\Workspace\model_zoo')

from zoo.backends.huggingface.roberta_language_detection.model import RobertaLanguageDetect


# def test_classification():
#     model = HuggingfacePipelineModel('text-classification',HUGGINGFACE, 'roberta-large-mnli')
#     ret = model("A soccer game with multiple males playing. Some men are playing a sport.")
#     assert ret[0]['label'] == 'ENTAILMENT'
#     return

# def test_distilbert_en():
#     model = HuggingfacePipelineModel('sentiment-analysis', HUGGINGFACE, 'distilbert-base-uncased-finetuned-sst-2-english')
#     ret = model("A soccer game with multiple males playing")
#     assert ret[0]['label'] == 'POSITIVE'
#     return

# def test_helsinki_en_zh():
#     model = HuggingfacePipelineModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-en-zh')
#     ret = model("My name is Wolfgang, and I live in Berlin.")
#     assert ret[0]['translation_text'] == '我叫沃尔夫冈 我住在柏林'
#     return

# def test_helsinki_zh_en():
#     model = HuggingfacePipelineModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-zh-en')
#     ret = model("我叫沃尔夫冈，我住在柏林。")
#     assert ret[0]['translation_text'] == 'My name is Wolfgang, and I live in Berlin.'
#     return

# def test_helsinki_de_en():
#     model = HuggingfacePipelineModel('translation', HUGGINGFACE, 'Helsinki-NLP--opus-mt-de-en')
#     ret = model("Schön dich kennenzulernen, mein Name ist Wolfgang.")
#     print(ret)
#     return

def test_papluca_xlm_roberta_base_language_detection():
    model = RobertaLanguageDetect()
    ret = model(["Jactos do exército matam 38 militantes em ataques aéreos no Noroeste do Paquistão"])
    print(ret)
    assert ret[0]['label'] == 'pt'
