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

BACKEND: PaddleNLP

可选模型：

| 模型 | 准确率| 数据集| 速度iters/s |
|-----|-------|-------|------|
|bilstm|83.75|ChnSentiCorp|235.3|
|skep_ernie_1.0_large_ch|90.08|ChnSentiCorp|2.8|
|uie-senta-base|94.35|ChnSentiCorp|1.4|

paddleNLP官方模型说明：https://github.com/PaddlePaddle/PaddleNLP/blob/develop/docs/model_zoo/taskflow.md 

### OCR

TASK：从图片中识别中英文文字

BACKEND：PaddleOCR

#### PaddleOCR
OCR流程分为三个独立模块，分别是文本检测(Text Detection)，方向分类器(Direction Classifier)，文本识别(Text Recognition)。

| 文本检测模型 | Hmean%| 模型大小MB|速度ms|
|-----|-------|-------|-------|
|PP-OCRv3|62.9|15.6|331|


### 翻译
中译英：Helsinki-NLP--opus-mt-zh-en
模型地址： https://huggingface.co/Helsinki-NLP/opus-mt-zh-en

英译中：Helsinki-NLP--opus-mt-en-zh
模型地址： https://huggingface.co/Helsinki-NLP/opus-mt-en-zh


| 模型 | BLEU| chr-F|速度ms|
|-----|-------|-------|-------|
|Helsinki-NLP--opus-mt-zh-en|36.1|0.548|-|
|Helsinki-NLP--opus-mt-en-zh|31.4|0.268|-|

### 语种识别
模型：papluca/xlm-roberta-base-language-detection
模型地址：https://huggingface.co/papluca/xlm-roberta-base-language-detection

## 计划

0. [X] CLIP: 20230530
1. [X] 语种识别
2. [X] 翻译
3. [X] 小语种翻译
4. [X] 情感分析
5. [X] OCR
6. [ ] LLAMA