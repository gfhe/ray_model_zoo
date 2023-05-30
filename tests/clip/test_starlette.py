from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.testclient import TestClient

# 创建一个 Starlette 应用
app = Starlette()

# 定义一个路由和处理函数
@app.route("/",methods=['post'])
async def homepage(request):
    print(f"{type(request)}")
    return JSONResponse({"message": "Hello, world!"})

# 使用 TestClient 进行测试
client = TestClient(app)
response = client.post("/", content=open("../../src/ray_model_zoo/models/clip/pokemon.jpeg", "rb").read())
print(response.status_code)
assert response.status_code == 200
assert response.json() == {"message": "Hello, world!"}