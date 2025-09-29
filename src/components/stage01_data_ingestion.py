#according to our data sources we write data_ingestion.py file code 
#here we are getting data from url and in some other cases we get data from Databases, or from cloud storage like AWS S3, GCP, AZURE etc
import os
import urllib.request as request
from zipfile import ZipFile
from src.logger.logging import logging
from src.exception import CustomException
from pathlib import Path
from tqdm import tqdm #library used to display smart progress bars for loops and iterations
from src.entity.config_entity import DataIngestionConfig
from src.utils.utils import get_size 


class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        

    def download_file(self):
        logging.info("Trying to download file...")
        if not os.path.exists(self.config.local_data_file):
            logging.info("Download started...")
            request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logging.info(f"File downloaded successfully from url: {self.config.source_URL} to local path: {self.config.local_data_file}")
        else:
            logging.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")        

            


    def _get_updated_list_of_files(self,list_of_files):
       return [f for f in list_of_files if f.endswith(".jpg") and ("Cat" in f or "Dog" in f)]
        

    def _preprocess(self, zf: ZipFile, f: str, working_dir: str):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)
        
        if os.path.getsize(target_filepath) == 0:
            logging.info(f"removing file:{target_filepath} of size: {get_size(Path(target_filepath))}")
            os.remove(target_filepath)

    def unzip_and_clean(self):
        logging.info(f"unzipping file and removing unawanted files")
        with ZipFile(file=self.config.local_data_file, mode="r") as zf:
            list_of_files = zf.namelist()
            updated_list_of_files = self._get_updated_list_of_files(list_of_files)
            for f in tqdm(updated_list_of_files):
                self._preprocess(zf, f, self.config.unzip_dir)