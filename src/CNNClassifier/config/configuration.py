from CNNClassifier.utils.utils import read_yaml, create_dir
from CNNClassifier.entity.config_entity import DataIngestionConfig,PrepareBaseModelConfig,TrainingConfig,EvaluationConig
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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
            config =self.config.PREPARE_BASE_MODEL

            create_dir([config.ROOT_DIR])

            prepare_base_model_config= PrepareBaseModelConfig(
                        root_dir=Path(config.ROOT_DIR),
                        base_model_path= Path(config.BASE_MODEL_PATH),
                        updated_base_model_path=Path(config.UPDATED_BASE_MODEL_PATH),
                        param_image_size=self.params.IMAGE_SIZE,
                        params_learning_rate=self.params.LEARNING_RATE,
                        param_include_top=self.params.INCLUDE_TOP,
                        param_weight=self.params.WEIGHTS,
                        param_class=self.params.CLASSES
                )
            return prepare_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        training = self.config.training
        prepare_base_model = self.config.PREPARE_BASE_MODEL
        params = self.params
        training_data = os.path.join(self.config.DATA_INGESTION.UNZIP_DIR, "PetImages")
        create_dir([Path(training.root_dir)])

        training_config = TrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.UPDATED_BASE_MODEL_PATH),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config 
    
    def get_validation_config(self) -> EvaluationConig:
           evaluation = self.config.EVALUATION
           eval_config = EvaluationConig(
                  path_of_model=evaluation.PATH_OF_TRAINED_MODEL,
                  training_data= evaluation.TRAINIG_DATA,
                  all_params= self.params,
                  params_image_size= self.params.IMAGE_SIZE,
                  params_batch_size= self.params.BATCH_SIZE
           )

           return eval_config
           

            

            
