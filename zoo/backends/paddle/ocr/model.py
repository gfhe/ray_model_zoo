from zoo.backends.base import Model
from zoo.task.ocr import OCR, task_name


class PaddleOCR(Model, OCR):

    def __init__(self, backend, model):
        super().__init__(task_name, backend, model)
        # TODO：init paddle ocr
        self.model = None

    def detect(self, image: bytes):
        self.model.detect(image)
