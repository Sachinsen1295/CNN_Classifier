from CNNClassifier.utils.utils import read_yaml, create_dir
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.constants import CONFIG_FILE_PATH, PARAM_FILE_PATH
from pathlib import Path
import os


class ConfigurationManager:
    def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAM_FILE_PATH):
                 self.config = read_yaml(config_filepath) # to read Yaml file from COnfig
                 self.params = read_yaml(params_filepath)
                 create_dir([self.config.ARTIFACTS_DIR])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
            config = self.config.DATA_INGESTION

            create_dir([config.ROOT_DIR])

            data_ingestion_config= DataIngestionConfig(
                                    root_dir=config.ROOT_DIR,
                                    source_url=config.SOURCE_URL,
                                    local_file_path=config.LOCAL_DATA_FILE,
                                    unzip_dir=config.UNZIP_DIR)
            return data_ingestion_config

            

            
