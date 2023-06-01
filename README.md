# ray_model_zoo

运行在 ray 框架的模型库。


## 使用说明

以clip模型为例。


## 开发流

1. 开发模型
2. 模型测试代码
3. 开发ray serve
4. ray serve 测试
5. 性能测试
6. 生成 ray serve 部署配置
7. 部署RayServices和RayCluster
8. 测试部署

### 生成RayServe 配置

`serve build zoo.model.clip.ray_serve:clip -k -o deploy/clip/clip_config.yaml`

> serve build 支持**多模型**同时部署

> ⚠️注意：生成的配置中，`routePrefix` 可能生成的**不**正确，需要确认清楚。

### 提交 ray job

## 开发规范

配置文件为`zoo/config/cofig.ini`，定义了模型和数据的存储路径

### 模型扩展
1. 在`zoo/model`中增加新的模型服务推理代码
    1. 模型封装：
        1. 默认的模型封装：`model.py`
        2. 不同类型backend的模型封装：`model_[backend_type].py`，例如 `model_torch.py`, `model_triton.py`。
    2. ray serve:
        1. 默认的模型的ray serve 封装：`ray_serve.py`
        2. 不同类型的backend 模型的ray serve 封装：`ray_serve_[backend_type].py.py`，例如 `ray_serve_torch.py`, `ray_serve_triton.py`:
2. 在`zoo/model/base.py` 中增加模型的名字和模型的不同参数级别；
3. 直接运行zoo中的代码：例如运行 `zoo/model/clip/model.py`, 使用 `python -m zoo.model.clip.model`
4. ray serve 本地测试： `serve run zoo.model.clip.ray_serve:clip`

### 模型单元测试

1. 在 `tests`中增加模型的测试类，包括模型、ray serve、压力测试三个部分。
2. 测试方法； 
   1. unittest 框架测试：在工程**根目录**下，运行：`python -m unittest test/clip/test_model.py` 或者 `python -m unittest test.clip.test_model`
   2. 可执行文件测试： 在工程**根目录**下，`python -m test.clip.test_ray_serve_client`

> 1. 压力测试：给出具体的**硬件配置**限制。
> 2. 压力测试：对比 ray serve 封装前后的性能。


## 支持的模型

### CLIP

TASK：特征提取[图、文]
BACKEND：pytorch、triton


### ...



## 计划
0. [X] CLIP: 20230530
1. [ ] 语种识别
2. [ ] 翻译
3. [ ] 小语种翻译
4. [ ] 情感分析
5. [ ] OCR
6. [ ] LLAMA