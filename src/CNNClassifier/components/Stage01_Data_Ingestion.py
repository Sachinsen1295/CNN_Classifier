import os
from urllib import request                          #to download from url
from zipfile import ZipFile                                  #to extract Zip file
from pathlib import Path
from tqdm import tqdm                                       # to have a process bar
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.utils import utils
from CNNClassifier.logger import logger

class DataIngestion:
    def __init__(self, config:DataIngestionConfig) -> None:
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_file_path):
            request.urlretrieve(
                url= self.config.source_url,
                filename= self.config.local_file_path
            )

        else:
            logger.info(f"file already exist {self.config.local_file_path}")


    def get_updated_list_file(self,list_of_files):
        return [f for f in list_of_files if f.endswith(".jpg")]

    def preprocess(self,zf,f,working_dir):
        target_file_path = os.path.join(working_dir,f)
        if not os.path.exists(target_file_path):
            zf.extract(f,working_dir)

    def unzip_clean(self):
        with ZipFile(file = self.config.local_file_path,mode='r') as zf:
            list_of_files = zf.namelist()
            updated_list_of_file= self.get_updated_list_file(list_of_files=list_of_files)
            for f in tqdm(updated_list_of_file):
                self.preprocess(zf,f,self.config.unzip_dir)


    

