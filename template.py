import os
import sys
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s]: %(message)s")

package_name = "CNNClassifier"

list_of_files=[
   ".github/workflows/.gitkeep",
   f"src/{package_name}/__init__.py", 
   f"src/{package_name}/components/__init__.py", 
   f"src/{package_name}/utils/__init__.py", 
   f"src/{package_name}/config/__init__.py", 
   f"src/{package_name}/pipeline/__init__.py", 
   f"src/{package_name}/entity/__init__.py", 
   f"src/{package_name}/constants/__init__.py",
   "tests/__init__.py",
   "tests/unit/__init__.py",
   "tests/integration/__init__.py",
   "configs/config.yaml",
   "params.yaml",
   "init_setup.sh",
   "requirements.txt", 
   "requirements_dev.txt",
   "setup.py",
   "setup.cfg",
   "pyproject.toml",
   "tox.ini",
   "research/trials.ipynb", 
                ]

for filepath in list_of_files:
    filepath = Path(filepath)
    file_dir , filename = os.path.split(filepath)

    if file_dir!="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"creating directory: {file_dir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open (filename, "w") as f:
            pass
            logging.info(f"creating filepath :{filepath}")

    else :
        logging.info(f"{filepath} already exists")

