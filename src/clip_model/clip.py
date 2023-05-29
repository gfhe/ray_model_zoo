import cn_clip.clip as clip
from cn_clip.clip import load_from_name, available_models

## 获取测试图片
#!wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg
# print("Available models:", available_models())  

# 封装 CN Clip 模型
from PIL import Image
from models import Model

class ClipModel(Model):
    def __init__(self):
      self.model, self.preprocess = load_from_name("ViT-B-16", device=super().device, download_root=super().model_dir)
        
    def encode_image(self, image_bytes):
        import io
        image = io.BytesIO(image_bytes)
        image = self.preprocess(Image.open(image)).unsqueeze(0).to(super().device)
        return self.model.encode_image(image)