from ray_model_zoo.clip import ClipModel

## 获取测试图片
# wget https://raw.githubusercontent.com/OFA-Sys/Chinese-CLIP/master/examples/pokemon.jpeg

# 测试模型
clip = ClipModel()
with open('./pokemon.jpeg', 'rb') as f:
    embedding = clip.encode_image(f.read())
    print(embedding.shape)
