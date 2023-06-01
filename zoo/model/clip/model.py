from cn_clip.clip import load_from_name

# 封装 CN Clip 模型
from PIL import Image
from zoo.model.base import Model, CN_CLIP


class ClipModel(Model):
    """
    模型：Chinese clip
    用途：图像
    github：https://github.com/OFA-Sys/Chinese-CLIP
    """

    def __init__(self):
        super().__init__(CN_CLIP)
        self.model, self.preprocess = load_from_name("ViT-B-16", device=self.device, download_root=self.model_dir)

    def encode_image(self, image_bytes):
        import io
        image = io.BytesIO(image_bytes)
        image = self.preprocess(Image.open(image)).unsqueeze(0).to(self.device)
        return self.model.encode_image(image)

    def encode_text(self, texts):
        pass
