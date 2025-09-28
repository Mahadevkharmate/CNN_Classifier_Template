from src.components.stage01_data_ingestion import DataIngestion
from src.config import ConfigurationManager
from src.logger.logging import logging
from src.exception import CustomException
from pathlib import Path
import sys

logging.info("Starting data ingestion stage")

config = ConfigurationManager()
data_ingestion_config = config.get_data_ingestion_config() # here we get all config defined in config.yaml
data_ingestion =DataIngestion(config = data_ingestion_config) #object of DataIngestion class
data_ingestion.download_file() #calling the method to download the file
data_ingestion.get_updated_list_of_files() #calling the method to get the updated list of  
data_ingestion.preprocess() #calling the method to preprocess the data
data_ingestion.unzip_and_clean() #calling the method to unzip and clean the data

logging.info("Completed data ingestion stage")