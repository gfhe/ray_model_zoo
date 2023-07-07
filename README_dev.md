# ray_model_zoo  开发说明

## 工程结构

```text
├── data
│  └── pokemon.jpeg
├── deploy
│  ├── clip
│  └── ray_cluster
├── LICENSE
├── model
│  └── cn_clip
├── README.md
├── README_dev.md
├── requirements.txt
├── test
│  ├── __init__.py
│  ├── __pycache__
│  ├── clip
│  └── starlette
└── zoo
   ├── __init__.py
   ├── __pycache__
   ├── cmd.py
   ├── config
   ├── model
   └── utils.py
```

1. zoo：源代码，
    1. cmd： 命令行工具
    2. config： 配置处理
    3. model： 模型和服务
    4. utils： 通用工具
2. test：测试代码，按模型组织
3. model：模型存储目录，按模型组织
4. data：数据目录，按模型组织
5. deploy：部署配置和脚本

## 开发流

1. 开发模型
2. 模型测试代码
3. 开发ray serve
4. ray serve 测试
5. 性能测试
6. 生成 ray serve 部署配置
7. 部署RayServices和RayCluster
8. 测试部署


### 注意事项

1. 每个module的`__init__.py`里面一般**不要**初始化类。
2. model_card 在本 model的module的`__init__.py` 导入。

### 测试

* 开发位置和命名： `text/[MODEL]/`
    * 模型功能测试： `test_model.py`
    * 模型性能测试：`test_benchmark_model.py`
    * ray serve 测试：`test_ray_serve.py`
    * ray serve 性能测试：`test_benchmark_ray_serve.py`
* 开发框架： `unittest`
* 测试方法；
    1. unittest 框架测试：在工程**根目录**下，运行：`python -m unittest test/clip/test_model.py`
       或者 `python -m unittest test.clip.test_model`
    2. 可执行文件测试： 在工程**根目录**下，`python -m test.clip.test_ray_serve_client`
    3. ray serve 本地运行： `serve run zoo.model.clip.ray_serve:clip`
    4. 客户端请求ray serve： `curl -v http://localhost:8000/clip/health`

### 生成RayServe 配置

`serve build zoo.model.clip.ray_serve:clip -k -o deploy/clip/clip_config.yaml`

> serve build 支持**多模型**同时部署

> ⚠️注意：
> 1. 生成的配置中，`routePrefix` 可能生成的**不**正确或者仅为默认值，需要确认清楚。
> 2. `@serve.deployment`中不要使用 `name` 参数，会造成`routePrefix` 不生效。

### 提交 ray job

```shell
ray job submit --working-dir ./zoo --address  http://10.208.63.33:32107 -- python zoo/model/clip/ray_serve.py
```

## 开发规范

配置文件为`zoo/config/cofig.ini`，定义了模型和数据的存储路径

### 模型扩展

1. 在`zoo/model`中增加新的模型服务推理代码
    1. 模型封装：
        1. 默认的模型封装：`model.py`
        2. 不同类型backend的模型封装：`model_[backend_type].py`，例如 `model_torch.py`, `model_triton.py`。
    2. ray serve:
        1. 默认的模型的ray serve 封装：`ray_serve.py`
        2. 不同类型的backend 模型的ray serve 封装：`ray_serve_[backend_type].py.py`
           ，例如 `ray_serve_torch.py`, `ray_serve_triton.py`:
2. 在`zoo/model/base.py` 中增加模型的名字和模型的不同参数级别；
3. 测试模型功能和ray serve 服务：
    1. 运行zoo中的代码：例如运行 `zoo/model/clip/model.py`, 使用 `python -m zoo.model.clip.model`
    2. ray serve 本地测试： `serve run zoo.model.clip.ray_serve:clip`

### 模型单元测试

1. 在 `tests`中增加模型的测试类，包括模型、ray serve、压力测试三个部分。
2. 测试方法；
    1. unittest 框架测试：在工程**根目录**下，运行：`python -m unittest test/clip/test_model.py`
       或者 `python -m unittest test.clip.test_model`
    2. 可执行文件测试： 在工程**根目录**下，`python -m test.clip.test_ray_serve_client`

> 1. 压力测试：给出具体的**硬件配置**限制。
> 2. 压力测试：对比 ray serve 封装前后的性能。
