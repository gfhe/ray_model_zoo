import requests

response = requests.post("http://127.0.0.1:8000/clip", data=open('./pokemon.jpeg', 'rb').read())
print(response.text)