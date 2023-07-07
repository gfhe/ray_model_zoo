import json
import unittest
from pathlib import Path

import httpx
import ray

from zoo.config import data_dir


class ClipServeTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.host = 'http://localhost:8000/clip'

    def test_clip_ray_serve_text(self):
        data = ["这是一只皮卡丘", "hello"]
        # headers = {"Content-Type": "application/json"}
        response = httpx.post(self.host + '/text', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), len(response.json()))

    def test_clip_ray_serve_image(self):
        files = []
        file_names = ['pokemon.jpeg']
        for file_name in file_names:
            files.append(('image', (file_name, open(Path(data_dir) / file_name, 'rb'), 'image/png')))

        # 发送POST请求
        response = httpx.post(self.host + '/image', files=files)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(files), len(response.json()))


if __name__ == '__main__':
    unittest.main()
