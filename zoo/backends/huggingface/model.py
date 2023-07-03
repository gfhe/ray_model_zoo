import logging
from typing import Any

from zoo.backends.base import Model
from zoo.backends.registry import HUGGINGFACE

logger = logging.getLogger(__name__)

class HuggingfacePipelineModel(Model):
    """
    封装Huggingface模型
    """

    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        from transformers import pipeline
        super().__init__(task=task, backend=backend, model=model)
        self.instance = pipeline(task=task, 
                                 model=self.model_path,
                                 **kwargs)
        logger.info(f"Huggingface pipeline model deployed.")

    def __call__(self, sentence):
        """
        调用模型
        Args:
            sentence (str): 要进行推理的文本
        Returns:
            result (List): 模型推理结果
        """
        return self.instance(sentence)

class HuggingfaceAutoModel(Model):
    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        from transformers import AutoTokenizer
        super().__init__(task=task, backend=backend, model=model)
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.device = kwargs.get('device', 'cpu')

class HuggingfaceAutoSeq2SeqLMModel(HuggingfaceAutoModel):
    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        from transformers import AutoModelForSeq2SeqLM
        super().__init__(task=task, backend=backend, model=model)
        self.instance = AutoModelForSeq2SeqLM.from_pretrained(self.model_path)
        logger.info(f"Huggingface HuggingfaceAutoSeq2SeqLMModel deployed.")
    
    def __call__(self, text):
        """
        调用模型
        Args:
            text (str): 要进行推理的文本
        Returns:
            result (List): 模型推理结果
        """
        encode_text = self.tokenizer(text, max_length=128, truncation=True, padding=True, return_tensors='pt').to(self.device)
        out = self.instance.generate(**encode_text, max_length=1024)
        out_text = self.tokenizer.decode(out[0])
        out_text = out_text.replace("<pad> ",'').replace("<pad>", "")
        return out_text

class HuggingfaceAutoSequenceClassificationModel(HuggingfaceAutoModel):
    def __init__(self, task, backend=HUGGINGFACE, model=None, **kwargs):
        from transformers import AutoModelForSequenceClassification
        super().__init__(task=task, backend=backend, model=model)
        self.instance = AutoModelForSequenceClassification.from_pretrained(self.model_path)
        logger.info(f"Huggingface HuggingfaceAutoSequenceClassificationModel deployed.")
    
    def __call__(self, text):
        encode_text = self.tokenizer(text, max_length=128, truncation=True, padding=True, return_tensors='pt').to(self.device)
        out = self.instance(**encode_text)
        return out