from enum import Enum


class Task(Enum):
    FeatureExtraction = 'feature-extraction'
    OCR = 'ocr'
    Translation = 'translation'
    LanguageDetection = 'language-detection'


class Backend(Enum):
    PYTORCH = "pytorch"
    PADDLE = "paddle"
    TENSORFLOW = "tensorflow"


if __name__ == '__main__':
    task = Task.FeatureExtraction
    print(task)
