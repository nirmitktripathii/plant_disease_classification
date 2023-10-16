import os
import urllib.request as request
import zipfile
import shutil
from plant_disease_classification import logger
from plant_disease_classification.utils.common import get_size
from plant_disease_classification.entity.config_entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")  


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        os.remove(self.config.local_data_file)

    def copy_dataset(self):
        destination_dir = self.config.destination_dir
        if not os.path.exists(destination_dir):
            shutil.copytree(self.config.source_dir, destination_dir)
            logger.info(f"{self.config.source_dir} copied!")         
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.unzip_dir))}")  



