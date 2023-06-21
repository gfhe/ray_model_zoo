# ray_model_zoo

运行在 ray 框架的模型库。[开发请参考开发文档](README_dev.md)

## 使用说明

以clip模型为例。

1. 获取 deployment 的route信息：`http://ip:8000/-/routes`

情感分析
1. 在model_zoo根目录下，运行`python zoo/model/paddlenlp_taskflow/ray_serve.py -m <model> -p <path-to-model>`
2. 运行`python zoo/model/paddlenlp_taskflow/ray_serve.py -h`查看帮助。

OCR
1. 在model_zoo根目录下，运行`python zoo/model/paddleocr/ray_serve.py -m <model> -p <path-to-model>`
2. 运行`python zoo/model/paddleocr/ray_serve.py -h`查看帮助。

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
4. [X] 情感分析
5. [X] OCR
6. [ ] LLAMA