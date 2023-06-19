from ray import serve
from fastapi import FastAPI, Request

from zoo.model.clip.ray_model import ClipRayModel
from zoo.model.base import Serve

app = FastAPI()


@serve.deployment(route_prefix="/clip",
                  autoscaling_config={
                      "min_replicas": 1,
                      "initial_replicas": 1,
                      "max_replicas": 10,
                      "target_num_ongoing_requests_per_replica": 5,
                      "upscale_delay_s": 10,
                      "downscale_delay_s": 10
                  },
                  ray_actor_options={"num_cpus": 0, "num_gpus": 0.5}
                  )
@serve.ingress(app)
class ClipModelServe(Serve):

    def __init__(self):
        self.ray_model = ClipRayModel()

    @app.post("/text")
    async def text_feature(self, request: Request):
        """
        文本向量表示推理：

        ` curl -v http://localhost:8000/clip/text -H "Content-Type: application/json" -d '["aaa","bbb"]'`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.text_feature`
        :param request: 请求体，Content-Type: application/json, body: ["text1", "text2"]
        :return: 向量表示，list
        """
        return await self.ray_model.text_feature(request)

    @app.post("/image")
    async def image_feature(self, request: Request):
        """
        图片向量表示推理

        `curl -v http://localhost:8000/clip/image -F "image=@/path/to/image" -F "image=@/path/to/image"`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.image_feature`
        :param request: 请求体，Content-Type: multipart/form-data, 支持上传多个图片，key=image
        :return: 向量表示，list
        """
        return await self.ray_model.image_feature(request)

    @app.get("/health")
    def health(self):
        # return super().health()
        return "ok"


clip = ClipModelServe.bind()

if __name__ == "__main__":
    handle = serve.run(clip, name="clip", host='0.0.0.0', port=8000)
