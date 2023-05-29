from clip import ClipModel

# 测试模型
clip = ClipModel()
with open('./pokemon.jpeg', 'rb') as f:
    embedding = clip.encode_image(f.read())
    print(embedding.shape)
