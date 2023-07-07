import configparser
from pathlib import Path
import logging
import os

_MODEL_DIR = "models"
_DATA_DIR = "data"

current_dir_path = os.path.dirname(os.path.abspath(__file__))

config = configparser.ConfigParser()
config.read(current_dir_path+'/config.ini')

default_profile = config.get("DEFAULT", 'profile')
ROOT_DIR = config.get(default_profile, 'root_dir')
logging.info(f"ZOO ROOT DIR: {ROOT_DIR}")

data_dir = Path(ROOT_DIR) / _DATA_DIR
model_dir = Path(ROOT_DIR) / _MODEL_DIR

__all__ = ['data_dir', 'model_dir']
