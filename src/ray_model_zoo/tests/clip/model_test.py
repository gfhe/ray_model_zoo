from ray_model_zoo.clip import ClipModel
import unittest

## 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

class ClipModelTest(unittest.TestCase):

    def __init__(self):
        self.clip = ClipModel()
    
    def test_image(self):
        with open('./pokemon.jpeg', 'rb') as f:
            embedding = self.clip.encode_image(f.read())
            print(embedding.shape)

if __name__ == '__main__':
    unittest.main()