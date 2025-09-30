import os
import yaml
import json
import joblib
from pathlib import Path
from typing import List
from src.logger.logging import logging
from typing import Any
from ensure import ensure_annotations
from box import ConfigBox
from src.exception import CustomException

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    try:
        with open(path_to_yaml, 'r') as file:
            content = yaml.safe_load(file)
            return ConfigBox(content)
    except Exception as e:
        logging.error(f"Error reading YAML file at {path_to_yaml}: {e}")
        raise CustomException(f"Error reading YAML file at {path_to_yaml}: {e}")

@ensure_annotations
def save_json(path_to_json: Path, data: Any) -> None:
    try:
        with open(path_to_json, 'w') as file:
            json.dump(data, file,indent=4)
        logging.info(f"JSON file saved at {path_to_json}")
    except Exception as e:
        logging.error(f"Error saving JSON file at {path_to_json}: {e}")
        raise CustomException(f"Error saving JSON file at {path_to_json}: {e}")

@ensure_annotations
def load_json(path_to_json: Path) -> Any:
    try:
        with open(path_to_json, 'r') as file:
            return json.load(file)
        logging.info(f"JSON file loaded from {path_to_json}")
    except Exception as e:
        logging.error(f"Error loading JSON file at {path_to_json}: {e}")
        raise CustomException(f"Error loading JSON file at {path_to_json}: {e}")

@ensure_annotations
def save_model(path_to_model: Path, model: Any) -> None:
    try:
        joblib.dump(model, path_to_model)
    except Exception as e:
        logging.error(f"Error saving model at {path_to_model}: {e}")
        raise CustomException(f"Error saving model at {path_to_model}: {e}")

@ensure_annotations
def load_model(path_to_model: Path) -> Any:
    try:
        return joblib.load(path_to_model)
    except Exception as e:
        logging.error(f"Error loading model at {path_to_model}: {e}")
        raise CustomException(f"Error loading model at {path_to_model}: {e}")

@ensure_annotations
def get_size(path_to_file: Path) -> int:
    try:
        return os.path.getsize(path_to_file)
    except Exception as e:
        logging.error(f"Error getting size of file at {path_to_file}: {e}")
        raise CustomException(f"Error getting size of file at {path_to_file}: {e}")

@ensure_annotations
def create_directory(path_to_directories: list):  # plain list, not List[Path]
    """
    Creates directories given a list of Path objects.
    Compatible with Python 3.11 + ensure_annotations.
    """
    for path in path_to_directories:
        if not isinstance(path, Path):  # plain Path type, never List[Path]
            raise TypeError(f"{path} is not a Path")
        path.mkdir(parents=True, exist_ok=True)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data

    Args:
        path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data
