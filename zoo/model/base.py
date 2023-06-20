from abc import ABC, abstractmethod
import logging

logger = logging.getLogger(__name__)

CN_CLIP = "cn_clip"

models = {
    CN_CLIP: {
        'RN50': {'param': '', 'url': ''},
        'ViT-B-16': {'param': '', 'url': ''},
        'ViT-L-14': {'param': '', 'url': ''},
        'ViT-L-14-336': {'param': '', 'url': ''},
        'ViT-H-14': {'param': '', 'url': ''},
    },
}


# def cn_clip_models():
#     """
#     clip 模型支持的不同参数级别的模型
#     """
#     from cn_clip.clip import available_models
#     return available_models()


class Model(ABC):
    def __init__(self, model_name, model_param=None):
        self.model_name = model_name
        self.model_param = model_param if model_param is not None else self.default_model_param_name()

        # 模型使用的硬件
        # self.device = "cuda" if torch.cuda.is_available() else "cpu"
        logger.info(f"model_name={self.model_name}, "
                    f"model_param={self.model_param}, "
                    f"model_dir={self.model_path()}, ")

    @abstractmethod
    def model_load_name(self) -> str:
        """
        框架加载模型时，使用的模型名字
        """
        raise NotImplementedError

    @abstractmethod
    def model_path(self) -> str:
        """
        模型存储路径（,相对于model 文件夹）

        :ref:`zoo.config.model_dir`
        """
        raise NotImplementedError

    @abstractmethod
    def available_models(self) -> list:
        """
        模型的不同参数级别名字列表
        """
        return [p for p, _ in models.get(self.model_name).items()]

    def default_model_param_name(self) -> str:
        """
        默认的模型名字：模型参数列表的第一个
        """

        assert self.model_name in models
        model_param_list = self.available_models()
        return model_param_list[0]


class Serve:
    def health(self):
        """
        暴露服务健康的endpoint， 每个serve 自己实现。
        """
        return {"status": "ok"}
