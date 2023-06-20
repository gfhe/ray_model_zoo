import json
import sys
import os
sys.path.append(os.path.dirname(os.path.realpath(__name__)))
import argparse

from ray import serve
from fastapi import FastAPI, Request

from zoo.model.paddlenlp_taskflow import PaddleNLPTaskflowModel
from zoo.model.base import Serve

app = FastAPI()
parser = argparse.ArgumentParser(description='PaddleNLP一键预测')
parser.add_argument('-t', '--task', help='任务名称，默认为sentiment_analysis', default='sentiment_analysis')
parser.add_argument('-m', '--model', help='模型名称，默认使用bilstm', default='bilstm')
parser.add_argument('-p', '--path', help='模型参数保存位置')
args = parser.parse_args()

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
class PaddleNLPTaskflowServe(Serve):

    def __init__(self, task, model, param):
        self.ray_model = PaddleNLPTaskflowModel(task=task, model=model, param=param)

    @app.post("/")
    async def senta(self, request: Request):
        data = await request.json()
        return self.ray_model.forward(json.loads(data))

    @app.get("/health")
    def health(self):
        return "ok"


paddle_taskflow = PaddleNLPTaskflowServe.bind(task=args.task, model=args.model, param=args.path)

if __name__ == "__main__":
    handle = serve.run(paddle_taskflow, name="senta", host='0.0.0.0', port=8000)
