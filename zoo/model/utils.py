from zoo.model.paddlenlp import PaddleNLPServe
from zoo.model.paddleocr import PaddleOCRServe

serve_map = {
    'PaddleNLPServe': PaddleNLPServe, 
    'PaddleOCRServe': PaddleOCRServe
}

def get_serve_class(serve: str):
    return serve_map[serve]