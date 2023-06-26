from fastapi import Request

from zoo.model import ClipModel


class ClipRayModel:

    def __init__(self):
        self.model = ClipModel()

    async def text_feature(self, request: Request):
        """
        文本向量表示推理：

        :ref:`zoo.model.clip.ClipModel.encode_text`
        :param request: 请求体，Content-Type: application/json, body: ["text1", "text2"]
        :return: 向量表示，list
        """
        # TODO: debug log
        print(f"REQUEST: {type(request)}")
        # 从请求体中取出图片二进制数据。
        texts = await request.json()
        print(f"REST body: {len(texts)}, type={type(texts)}")
        # 注意！！！！！！ torch 数据无法通过http 传输
        text_embeddings = self.model.encode_text(texts)
        # TODO: debug log
        print(f"result shape: {text_embeddings.shape},{type(text_embeddings)}")
        return text_embeddings.cpu().detach().numpy().tolist()

    async def image_feature(self, request: Request):
        """
        图片向量表示推理

        :ref:`zoo.model.clip.ClipModel.encode_image`
        :param request: 请求体，Content-Type: multipart/form-data, 支持上传多个图片，key=image
        :return: 向量表示，list
        """
        form = await request.form()
        images = form.getlist('image')
        # TODO: debug log
        print(f"images: {images}")
        images_bytes = [await image.read() for image in images]
        image_embeddings = self.model.encode_image(images_bytes)
        # TODO: debug log
        return image_embeddings.cpu().detach().numpy().tolist()
