# ray_model_zoo

运行在 ray 框架的模型库。


## 开发规范

配置文件为`src/config/cofig.ini`，定义了模型和数据的存储路径

### 模型扩展
1. 在`src/models`中增加新的模型服务推理代码
    1. 模型封装：
        1. 默认的模型封装：`model.py`
        2. 不同类型backend的模型封装：`model_[backend_type].py`，例如 `model_torch.py`, `model_triton.py`。
    2. ray serve:
        1. 默认的模型的ray serve 封装：`ray_serve.py`
        2. 不同类型的backend 模型的ray serve 封装：`ray_serve_[backend_type].py.py`，例如 `ray_serve_torch.py`, `ray_serve_triton.py`:
2. 在`src/models/base.py` 中增加模型的名字和模型的不同参数级别；

### 模型单元测试

1. 在 `tests`中增加模型的测试类，包括模型、ray serve、压力测试三个部分。
2. 测试方法； 在工程**根目录**下，运行：`python -m unittest tests/clip/test_model.py` 

> 1. 压力测试：给出具体的**硬件配置**限制。
> 2. 压力测试：对比 ray serve 封装前后的性能。

## 支持的模型

### CLIP

TASK：特征提取[图、文]
BACKEND：pytorch、triton


### 



## 计划
0. [X] CLIP: 20230530
1. [ ] 语种识别
2. [ ] 翻译
3. [ ] 小语种翻译
4. [ ] 情感分析
5. [ ] OCR