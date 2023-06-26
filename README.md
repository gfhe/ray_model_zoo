# ray_model_zoo

运行在 ray 框架的模型库。[开发请参考开发文档](README_dev.md)

## 使用说明

以clip模型为例。

1. 获取 deployment 的route信息：`http://ip:8000/-/routes`

## 支持的模型

### CLIP

TASK：特征提取[图、文]
BACKEND：pytorch、triton

### 情感分析

TASK: 分析中英文文本的情感倾向（正面/负面）

BACKEND: paddle

可选模型：
| 模型 | 准确率| 数据集| 速度iters/s |
|-----|-------|-------|------|
|bilstm|83.75|ChnSentiCorp|235.3
|skep_ernie_1.0_large_ch|90.08|ChnSentiCorp|2.8|

paddleNLP官方模型说明：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md 

## 计划

0. [X] CLIP: 20230530
1. [ ] 语种识别
2. [ ] 翻译
3. [ ] 小语种翻译
4. [X] 情感分析
5. [X] OCR
6. [ ] LLAMA