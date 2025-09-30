# Constants for file paths
from pathlib import Path

CONFIG_FILE_PATH = Path("configs/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
ARTIFACTS_DIR = Path("artifacts")
DATA_INGESTION_DIR = ARTIFACTS_DIR / "data_ingestion"
PREPARE_BASE_MODEL_DIR = ARTIFACTS_DIR / "prepare_base_model"
