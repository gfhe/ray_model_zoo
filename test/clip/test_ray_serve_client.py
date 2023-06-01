import requests
from zoo.config import data_dir
from pathlib import Path

response = requests.post("http://127.0.0.1:8000/clip", data=open(Path(data_dir) /'pokemon.jpeg', 'rb').read())
print(response.text)