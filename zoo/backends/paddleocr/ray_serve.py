from ray import serve
from fastapi import FastAPI, Request

from zoo.backends.paddleocr import PaddleOCRModel
from zoo.backends.base import Serve
from zoo.backends.registry import PADDLE_OCR


app = FastAPI()

@serve.ingress(app)
class PaddleOCRServe(Serve):
    backend = PADDLE_OCR
    def __init__(self, task, model, **kwargs):
        self.ray_model = PaddleOCRModel(task=task, backend=self.backend, model=model, **kwargs)

    @app.post("/")
    async def ocr(self, request: Request):
        data = await request.body()
        return self.ray_model(data)

    @app.get("/health")
    def health(self):
        return "ok"