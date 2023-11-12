import os
import sys
import yaml
from CNNClassifier.logger import logger
import json
import joblib
from pathlib import Path
from typing import Any
from ensure import ensure_annotations   # to fix the output in what format to receive 
from box.exceptions import BoxValueError
from box import ConfigBox
import tensorflow as tf
from tqdm import tqdm                                       # to have a process bar



@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    with open(path_to_yaml, "rb") as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    
@ensure_annotations
def save_json(path:Path , data) :
    with open (path ,"w") as data_json:
        json.dump(data,data_json, indent=4)
    


@ensure_annotations
def load_json():
    pass

#@ensure_annotations
def save_model(path:Path , model:tf.keras.Model()):
    model.save(str(path))

@ensure_annotations
def load_model():
    pass

@ensure_annotations
def get_size():
    pass

@ensure_annotations
def create_dir(path_to_directory:list, verbose=True):
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Create directory ay : {path}")
    



