from zoo.backends.base import Model, ModelCard
from zoo.task.ocr import OCR


class PaddleOCR(Model, OCR):

    @property
    def device(self):
        #TODO:
        return 0

    @classmethod
    def model_card(cls) -> ModelCard:
        pass

    def __init__(self, backend, model):
        super().__init__(OCR.task, backend, model)
        # TODO：init paddle ocr
        self.model = None

    def detect(self, image: bytes):
        self.model.detect(image)
