import unittest
import os, sys

# 将 src 目录加入 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))
from src.models.clip import ClipModel
from src.config import data_dir


# 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

class ClipModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.clip = ClipModel()

    def test_image(self):
        with open(data_dir+'/pokemon.jpeg', 'rb') as f:
            embedding = self.clip.encode_image(f.read())
            print(embedding.shape)


if __name__ == '__main__':
    unittest.main()
