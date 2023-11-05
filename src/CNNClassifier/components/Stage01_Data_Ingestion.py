import os
from urllib.request import Request                          #to download from url
from zipfile import ZipFile                                  #to extract Zip file
from pathlib import Path
from tqdm import tqdm                                       # to have a process bar
from CNNClassifier.entity.config_entity import DataIngestionConfig
from CNNClassifier.utils import utils
from CNNClassifier.logger import logger

class DataIngestion:
    def __init__(self) -> None:
        pass

    def download_file(self):
        pass

    def get_updated_list_file(self):
        pass

    def preprocess(self):
        pass

    def unzip(self):
        pass


    

