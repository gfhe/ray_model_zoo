import json

from ray import serve
from fastapi import FastAPI, Request

from zoo.model.paddlenlp import PaddleNLPModel
from zoo.model.base import Serve
from zoo.model.registry import PADDLE_NLP


app = FastAPI()
@serve.deployment(route_prefix="/senta",
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
class PaddleNLPServe(Serve):

    def __init__(self, task='sentiment_analysis', model_name='bilstm'):
        self.ray_model = PaddleNLPModel(task=task, model_lib=PADDLE_NLP, model_name=model_name)

    @app.post("/")
    async def senta(self, request: Request):
        data = await request.json()
        return self.ray_model(json.loads(data))

    @app.get("/health")
    def health(self):
        return "ok"
