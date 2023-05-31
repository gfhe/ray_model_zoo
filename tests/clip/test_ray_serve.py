import unittest
import ray
from ray import serve
import os, sys

# 将 src 目录加入 sys.path 中
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", "src")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src", "models")))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src", "config")))
from src.models.clip.ray_serve import clip
from src.config import data_dir


class ClipServeTest(unittest.TestCase):
    def test_clip_ray_serve(self):
        handle = serve.run(clip)
        with open(data_dir+'./pokemon.jpeg', 'rb') as f:
            result = ray.get(handle.encode_image.remote(image_bytes=f.read()))
            print(result)

if __name__ == '__main__':
    unittest.main()
