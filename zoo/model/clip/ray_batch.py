from ray import serve
from fastapi import FastAPI, Request

from zoo.model.clip.ray_model import ClipRayModel
from zoo.model.base import Serve


class ClipBatch:

    def __init__(self):
        self.ray_model = ClipRayModel()

    @serve.batch(max_batch_size=64)
    async def text_feature(self, request: Request):
        """
        文本向量表示推理：

        ` curl -v http://localhost:8000/text -H "Content-Type: application/json" -d '["aaa","bbb"]'`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.text_feature`
        :param request: 请求体，Content-Type: application/json, body: ["text1", "text2"]
        :return: 向量表示，list
        """
        return await self.ray_model.text_feature(request)

    @serve.batch(max_batch_size=32)
    async def image_feature(self, request: Request):
        """
        图片向量表示推理

        `curl -v http://localhost:8000/image -F "image=@/path/to/image" -F "image=@/path/to/image"`

        :ref:`zoo.model.clip.ray_model.ClipRayModel.image_feature`
        :param request: 请求体，Content-Type: multipart/form-data, 支持上传多个图片，key=image
        :return: 向量表示，list
        """
        return await self.ray_model.image_feature(request)


if __name__ == "__main__":
    serve.start()
