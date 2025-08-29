import os
from pathlib import Path
import logging


#defining logging 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

package_name = "cnn_classifier_template"

list_of_files = [
    ".github/workflows/.gitkeep",
   "src/__init__.py", 
   "src/components/__init__.py", 
   "src/utils/__init__.py", 
   "src/config/__init__.py", 
   "src/pipeline/__init__.py", 
   "src/entity/__init__.py", 
   "src/constants/__init__.py",
   "src/model.py",
   "src/train.py",
   "src/evaluate.py",
   "src/predict.py",
   "data/__init__.py",
   "data/raw/__init__.py",
   "data/processed/__init__.py",
   "notebooks/__init__.py",
   "notebooks/01_data_analysis.ipynb",
   "notebooks/02_model_training.ipynb",
   "notebooks/03_model_evaluation.ipynb",
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
   "deployment/__init__.py",
   "deployment/app.py", # FastAPI app for inference
   "deployment/Dockerfile", # Docker configuration
   "deployment/requirements.txt", # Python dependencies
   "deployment/config.py" # Configurations
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
    
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info("creating directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
            logging.info("creating empty file: {filepath}")
    else:
        logging.info("{filepath} already exists")
      

