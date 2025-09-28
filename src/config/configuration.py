from src.utils.utils import read_yaml, create_directory
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path
from src.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH

class ConfigurationManager:
    def __init__(self):
        self.config = read_yaml(CONFIG_FILE_PATH) #config.yaml file read

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config["data_ingestion"]
        return DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_URL"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"])
        )
