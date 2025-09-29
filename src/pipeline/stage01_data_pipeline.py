from src.components.stage01_data_ingestion import DataIngestion
from src.config.configuration import ConfigurationManager
from src.logger.logging import logging
from src.exception import CustomException
from pathlib import Path
import sys

logging.info("Starting data ingestion stage")
STAGE_NAME = "Data Ingestion stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config() # here we get all config defined in config.yaml
    data_ingestion =DataIngestion(config = data_ingestion_config) #object of DataIngestion class
    data_ingestion.download_file() #calling the method to download the file
    data_ingestion.unzip_and_clean() #calling the method to unzip and clean the data

if __name__ == '__main__':
    try:
        logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        main()
        logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
