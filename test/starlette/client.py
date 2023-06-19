import requests
from zoo.config import data_dir
from pathlib import Path

url = 'http://localhost:8000/clip/image'
images = [('image', ('image1.jpeg', open(Path(data_dir) / 'pokemon.jpeg', 'rb'))),
          ('image', ('image2.jpeg', open(Path(data_dir) / 'pokemon.jpeg', 'rb')))]
response = requests.post(url, files=images)
print(response.text)
