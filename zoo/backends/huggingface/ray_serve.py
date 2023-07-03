import json

from ray import serve
from fastapi import FastAPI, Request

from zoo.backends.huggingface import HuggingfacePipelineModel
from zoo.backends.base import Serve
from zoo.backends.registry import HUGGINGFACE


app = FastAPI()

@serve.ingress(app)
class HuggingfaceServe(Serve):
    backend = HUGGINGFACE
    def __init__(self, task, model, backend_model, **kwargs):
        if backend_model == 'HuggingfacePipelineModel':
            self.ray_model = HuggingfacePipelineModel(task=task, backend=self.backend, model=model, **kwargs)
        # TODO: 要不要保留非pipeline的用法？
        # else:
        #     self.ray_model = HuggingfaceAutoModel(task=task, backend=self.backend, model=model, **kwargs)

    @app.post("/")
    async def infer(self, request: Request):
        data = await request.json()
        return self.ray_model(json.loads(data))

    @app.get("/health")
    def health(self):
        return "ok"
