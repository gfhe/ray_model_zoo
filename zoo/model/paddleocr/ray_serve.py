import json

from ray import serve
from fastapi import FastAPI, Request

from zoo.model.paddleocr import PaddleOCRModel
from zoo.model.base import Serve
from zoo.model.registry import PADDLE_OCR


app = FastAPI()

@serve.deployment(route_prefix="/ocr",
                  autoscaling_config={
                      "min_replicas": 1,
                      "initial_replicas": 1,
                      "max_replicas": 2,
                      "target_num_ongoing_requests_per_replica": 5,
                      "upscale_delay_s": 10,
                      "downscale_delay_s": 10
                  },
                  ray_actor_options={"num_cpus": 1.0, "num_gpus": 0.0}
                  )
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
