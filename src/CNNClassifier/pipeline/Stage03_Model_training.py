from CNNClassifier.components.Stage03_trainning import Training
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.logger import logger
from CNNClassifier.constants import *

try:
    config = ConfigurationManager()

    training_config = config.get_training_config()
    training = Training(config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train()
    
except Exception as e:
    raise e


