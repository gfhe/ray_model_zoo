# ray_model_zoo

运行在 ray 框架的模型库。


## 开发规范

配置文件为`src/config/cofig.ini`，定义了模型和数据的存储路径

### 模型扩展
1. 在`src/models`中增加新的模型服务推理代码（模型定义和ray serve）
2. 在`src/models/base.py` 中增加模型的名字和模型的不同参数级别；

### 模型单元测试

1. 在 `tests`中增加模型的测试类，包括模型、ray serve、压力测试三个部分。
2. 测试方法； 在工程**根目录**下，运行：`python -m unittest tests/clip/test_model.py` 

> 1. 压力测试：给出具体的**硬件配置**限制。
> 2. 压力测试：对比 ray serve 封装前后的性能。

## 支持的模型

