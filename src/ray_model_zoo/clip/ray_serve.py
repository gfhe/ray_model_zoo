import ray
from ray import serve
from starlette.requests import Request

from ray_model_zoo.clip.model import ClipModel

@serve.deployment(name='clip', route_prefix="/clip")
class ClipModelDeployment:
    def __init__(self):
        self.model = ClipModel()
        
    def encode_image(self, image_bytes):
        return self.model.encode_image(image_bytes)

    async def __call__(self, request:Request):
        """
        封装请求
        """
        breakpoint()
        print(f"REQUEST: {type(request)}")
        #从请求体中取出图片二进制数据。
        body = await request.body()
        if len(body) <1:
            return
        print(f"REST body: {len(body)}, type={type(body)}")
        # 注意！！！！！！ torch 数据无法通过http 传输
        result = self.encode_image(body)
        print(f"result shape: {result.shape},{type(result)}")
        return result.detach().numpy().tolist()

# 部署模型servering
clip = ClipModelDeployment.bind()
# serve.start()
# ClipModelDeployment.deploy()

# time.sleep(3600.0)


# 运行ray serve， 默认服务在8000端口，dashboard 在 8265
# serve run clip_deploy:clip

# 测试 curl -XPOST http://127.0.0.1:8000/clip -H "Content-Type:image/jpeg" --data-binary "@./pokemon.jpeg"