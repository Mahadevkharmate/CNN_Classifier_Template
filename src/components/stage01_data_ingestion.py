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
from src.utils import utils

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config = config
        

    def download_file(self):
        pass


    def get_updated_list_of_files(self):
        pass

    def preprocess(self):
        pass

    def unzip_and_clean(self):
        pass
    