import unittest
from pathlib import Path

from zoo.model import ClipModel
from zoo.config import data_dir


# 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

class ClipModelTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("set up test class")
        cls.clip = ClipModel()

    def test_image(self):
        images_bytes = []
        for i in range(2):
            with open(Path(data_dir) / 'pokemon.jpeg', 'rb') as f:
                images_bytes.append(f.read())
        embedding = self.clip.encode_image(images_bytes)
        print(embedding.shape)
        self.assertEqual(embedding.shape[1], 1024)

    def test_text(self):
        embedding = self.clip.encode_text(["这是一只皮卡丘", "hello"])
        print(embedding.shape)
        self.assertEqual(embedding.shape[1], 1024)


if __name__ == '__main__':
    unittest.main()
