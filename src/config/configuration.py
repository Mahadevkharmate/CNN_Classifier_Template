from src.utils.utils import read_yaml, create_directory
from src.entity.config_entity import DataIngestionConfig
from pathlib import Path
from src.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH

class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath) #config.yaml file read
        self.params = read_yaml(params_filepath) #params.yaml file read
        create_directory([Path(self.config["artifacts_root"])]) #create artifacts directory

    def get_data_ingestion_config(self) -> DataIngestionConfig: #return type is DataIngestionConfig
        config = self.config["data_ingestion"] #getting data_ingestion section from config.yaml file
        create_directory([Path(config["root_dir"])]) #create root_dir directory of data_ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_URL"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"])
        )
        return data_ingestion_config
