import requests
from zoo.config import data_dir
from pathlib import Path

img_byte = [open(Path(data_dir) / 'pokemon.jpeg', 'rb').read(), open(Path(data_dir) / 'pokemon.jpeg', 'rb').read()]
response = requests.post("http://10.208.63.33:31146/clip/image", data=img_byte)
print(response.text)
