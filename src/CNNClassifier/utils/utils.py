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



@ensure_annotations
def read_yaml(path_to_yaml : Path) -> ConfigBox:
    with open(path_to_yaml, "rb") as yaml_file:
        content = yaml.safe_load(yaml_file)
        return ConfigBox(content)
    
@ensure_annotations
def save_json():
    pass

@ensure_annotations
def load_json():
    pass

@ensure_annotations
def save_mode():
    pass

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
    



