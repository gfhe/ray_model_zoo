import json

from ray import serve
from fastapi import Request, FastAPI

from zoo.backends.paddlenlp import PaddleNLPModel
from zoo.backends.base import Serve
from zoo.backends.registry import PADDLE_NLP


app = FastAPI()

@serve.ingress(app)
class PaddleNLPServe(Serve):
    backend = PADDLE_NLP
    def __init__(self, task, model='bilstm', **kwargs):
        self.ray_model = PaddleNLPModel(task=task, backend=self.backend, model=model, **kwargs)

    @app.post("/")
    async def senta(self, request: Request):
        data = await request.json()
        return self.ray_model(json.loads(data))

    @app.get("/health")
    def health(self):
        return "ok"
