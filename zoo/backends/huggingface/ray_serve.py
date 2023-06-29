import json

from ray import serve
from fastapi import FastAPI, Request

from zoo.backends.huggingface import HuggingfaceModel
from zoo.backends.base import Serve
from zoo.backends.registry import HUGGINGFACE


app = FastAPI()

@serve.ingress(app)
class HuggingfaceServe(Serve):
    backend = HUGGINGFACE
    def __init__(self, task, model, **kwargs):
        self.ray_model = HuggingfaceModel(task=task, backend=self.backend, model=model, **kwargs)

    @app.post("/")
    async def infer(self, request: Request):
        data = await request.json()
        return self.ray_model(json.loads(data))

    @app.get("/health")
    def health(self):
        return "ok"
