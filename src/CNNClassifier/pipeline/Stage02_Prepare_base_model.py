from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.Stage02_Prepare_base_Model import PrepareBaseModel
from CNNClassifier.exception import CustomException
import os,sys
from CNNClassifier.logger import logger

try: 
    #logger.info("STAGE02_pipeline stated")
    config = ConfigurationManager()

    get_base_model_config = config.get_prepare_base_model_config()

    prepare_base_model = PrepareBaseModel(config= get_base_model_config)
    prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()

except Exception as e:
    #logger.info("ERROR OCCURED IN PIPELINE")
    #raise CustomException(e,sys)
    raise e