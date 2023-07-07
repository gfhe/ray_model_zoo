from ray import serve
from fastapi import FastAPI, Request
import logging

from zoo.backends.pytorch.cn_clip.model import ClipModel
from zoo.backends.base import Serve

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
                  ray_actor_options={"num_cpus": 1, "num_gpus": 0}
                  )
@serve.ingress(app)
class ClipModelServe(Serve):

    def __init__(self):
        self.model = ClipModel()

    @app.post("/text")
    async def text_features(self, request: Request):
        """
        文本向量表示推理：

        ` curl -v http://localhost:8000/clip/text -H "Content-Type: application/json" -d '["aaa","bbb"]'`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.text_feature`
        :param request: 请求体，Content-Type: application/json, body: ["text1", "text2"]
        :return: 向量表示，list
        """
        texts = await request.json()
        logging.debug(f"REST body: {len(texts)}, type={type(texts)}")
        text_embeddings = self.model.text_features(texts)
        logging.debug(f"result shape: {text_embeddings.shape},{type(text_embeddings)}")
        return text_embeddings.cpu().detach().numpy().tolist()

    @app.post("/image")
    async def image_features(self, request: Request):
        """
        图片向量表示推理

        `curl -v http://localhost:8000/clip/image -F "image=@/path/to/image" -F "image=@/path/to/image"`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.image_feature`
        :param request: 请求体，Content-Type: multipart/form-data, 支持上传多个图片，key=image
        :return: 向量表示，list
        """
        form = await request.form()
        images = form.getlist('image')
        logging.debug(f"images size: {len(images)}")
        images_bytes = [await image.read() for image in images]
        image_embeddings = self.model.image_features(images_bytes)
        return image_embeddings.cpu().detach().numpy().tolist()

    @app.get("/health")
    def health(self):
        return "ok"


clip = ClipModelServe.bind()

if __name__ == "__main__":
    handle = serve.run(clip, name="clip", host='0.0.0.0', port=8000)
