import unittest
from src.ray_model_zoo.models.clip import ClipModel


## 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

class ClipModelTest(unittest.TestCase):

    def __init__(self):
        super().__init__()
        self.clip = ClipModel()

    def test_image(self):
        with open('../../models/clip/pokemon.jpeg', 'rb') as f:
            embedding = self.clip.encode_image(f.read())
            print(embedding.shape)


# if __name__ == '__main__':
#     unittest.main()
clip = ClipModel()
with open('../../models/clip/pokemon.jpeg', 'rb') as f:
    embedding = clip.encode_image(f.read())
    print(embedding.shape)
