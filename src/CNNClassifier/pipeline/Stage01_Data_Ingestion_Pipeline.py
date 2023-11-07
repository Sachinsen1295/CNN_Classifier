from CNNClassifier.components.Stage01_Data_Ingestion import DataIngestion
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.logger import logger


logger.info(f"Date Ingestion started")
config = ConfigurationManager()

data_ingestion_config = config.get_data_ingestion_config()

data_ingestion= DataIngestion(config=data_ingestion_config)

data_ingestion.download_file()
data_ingestion.unzip_clean()

logger.info(f"Data ingestion complete")






