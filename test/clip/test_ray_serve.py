import unittest
from pathlib import Path

import ray
from ray import serve

from zoo.config import data_dir
from zoo.backends.clip.ray_serve import clip


class ClipServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.handle = serve.run(clip)

    def test_clip_ray_serve_image(self):
        with open(Path(data_dir) / 'pokemon.jpeg', 'rb') as f:
            embedding = ray.get(self.handle.encode_image.remote(image=[f.read()]))
            print(embedding)
            self.assertEqual(embedding.shape[1], 1024)

    def test_clip_ray_serve_text(self):
        embedding = ray.get(self.handle.encode_text.remote(text=["这是一只皮卡丘", "hello"]))
        print(embedding)
        self.assertEqual(embedding.shape[1], 1024)


if __name__ == '__main__':
    unittest.main()
