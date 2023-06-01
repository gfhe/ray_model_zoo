from ray import serve
from starlette.requests import Request

from zoo.model import ClipModel


@serve.deployment(name='clip', route_prefix="/clip")
class ClipModelServe:
    def __init__(self):
        self.model = ClipModel()

    def encode_image(self, image_bytes):
        return self.model.encode_image(image_bytes)

    async def __call__(self, request: Request):
        """
        封装请求
        """
        # debug ray application
        # breakpoint()
        print(f"REQUEST: {type(request)}")
        # 从请求体中取出图片二进制数据。
        body = await request.body()
        if len(body) < 1:
            return
        print(f"REST body: {len(body)}, type={type(body)}")
        # 注意！！！！！！ torch 数据无法通过http 传输
        result = self.encode_image(body)
        print(f"result shape: {result.shape},{type(result)}")
        return result.detach().numpy().tolist()


clip = ClipModelServe.bind()
