import unittest
import ray
from ray import serve
from zoo.model.clip.ray_serve import clip
from zoo.config import data_dir


class ClipServeTest(unittest.TestCase):
    def test_clip_ray_serve(self):
        handle = serve.run(clip)
        with open(data_dir + './pokemon.jpeg', 'rb') as f:
            result = ray.get(handle.encode_image.remote(image_bytes=f.read()))
            print(result)


if __name__ == '__main__':
    unittest.main()
