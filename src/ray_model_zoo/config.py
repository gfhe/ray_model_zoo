import configparser

MODEL_DIR = "zoo_models"
DATA_DIR = "zoo_data"


config = configparser.ConfigParser()
config.read('config.ini')

data_dir = config.get('paths', DATA_DIR)
model_dir = config.get('paths', MODEL_DIR)