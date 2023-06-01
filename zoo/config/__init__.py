import configparser
from pathlib import Path

MODEL_DIR = "model"
DATA_DIR = "data"
ROOT_DIR = '/Users/hgf/Projects/py/ray_model_zoo'

# config = configparser.ConfigParser()
# config.read('config.ini')
#
# data_dir = config.get('paths', DATA_DIR)
# model_dir = config.get('paths', MODEL_DIR)

data_dir = Path(ROOT_DIR) / DATA_DIR
model_dir = Path(ROOT_DIR) / MODEL_DIR

__all__ = ['data_dir', 'model_dir']
