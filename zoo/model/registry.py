CN_CLIP = "cn_clip"
PADDLE_OCR = "paddleocr"
PADDLE_NLP = "paddlenlp"

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
            'PP-OCRv3': {'param': '', 'url': ''}
        },
    },
    'SentimentAnalysis':{
        PADDLE_NLP: {
            'bilstm': {'param': '', 'url': ''}
        }
    }
}

TASKS = [t for t in registry]
