from cn_clip.clip import load_from_name

# 封装 CN Clip 模型
from PIL import Image
from src.ray_model_zoo.models import Model, CN_CLIP


class ClipModel(Model):
    def __init__(self):
        super().__init__(CN_CLIP)
        self.model, self.preprocess = load_from_name("ViT-B-16", device=self.device, download_root=self.model_dir)

    def encode_image(self, image_bytes):
        import io
        image = io.BytesIO(image_bytes)
        image = self.preprocess(Image.open(image)).unsqueeze(0).to(self.device)
        return self.model.encode_image(image)
