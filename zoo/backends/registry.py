CN_CLIP = "cn_clip"
PADDLE_OCR = "paddleocr"
PADDLE_NLP = "paddlenlp"
HUGGINGFACE = 'huggingface'

# 任务类型 - 模型库 - 模型名称
registry = {
    'FeatureExtraction': {
        CN_CLIP: {
            'RN50': {'param': '', 'url': ''},
            'ViT-B-16': {'param': '', 'url': ''},
            'ViT-L-14': {'param': '', 'url': ''},
            'ViT-L-14-336': {'param': '', 'url': ''},
            'ViT-H-14': {'param': '', 'url': ''},
        }
    },
    'OCR': {
        PADDLE_OCR: {
            'default_serve': 'PaddleOCRServe',
            'models': {
                'PP-OCRv3': {'param': '', 'url': ''}
            }
        },
    },
    'SentimentAnalysis':{
        PADDLE_NLP: {
            'default_serve': 'PaddleNLPServe',
            'task_alias': 'sentiment_analysis', 
            'models': {
                'bilstm': {'param': '', 'url': ''},
                'skep_ernie_1.0_large_ch': {'param': '', 'url': ''}, 
                'uie-senta-base': {'param': ['schema'], 'url': ''},
            }
        },
        HUGGINGFACE: {
            'default_serve': 'HuggingfaceServe',
            'task_alias': 'sentiment-analysis',
            'models': {
                'distilbert-base-uncased-finetuned-sst-2-english': {'param': '', 'url': '', 'backend_model': 'HuggingfacePipelineModel'}
            }
        }
    },
    'NaturalLanguageInference': {
        HUGGINGFACE: {
            'default_serve': 'HuggingfaceServe',
            'task_alias': 'text-classification',
            'models': {
                'roberta-large-mnli': {'param': '', 'url': '', 'backend_model': 'HuggingfacePipelineModel'}
            }
        }
    },
    'Translation': {
        HUGGINGFACE: {
            'task_alias': 'translation', 
            'default_serve': 'HuggingfaceServe',
            'models': {
                'Helsinki-NLP--opus-mt-zh-en': {'param': '', 'url': '', 'backend_model': 'HuggingfaceAutoModel'}, 
                'Helsinki-NLP--opus-mt-en-zh': {'param': '', 'url': '', 'backend_model': 'HuggingfaceAutoModel'}, 
                'Helsinki-NLP--opus-mt-de-en': {'param': '', 'url': '', 'backend_model': 'HuggingfacePipelineModel'}, 
            }
        }
    },
    'LanguageDetection': {
        HUGGINGFACE: {
            'task_alias': 'text-classification',
            'default_serve': 'HuggingfaceServe',
            'models': {
                'papluca--xlm-roberta-base-language-detection': {'param': '', 'url': '', 'backend_model': 'HuggingfacePipelineModel'}
            }
        }
    }
}
