# importing the relevant libraries
from src.wine_quality.pipeline.data_ingestion_pipeline import *
from src.wine_quality import logger
import urllib.request as request
import os
import zipfile

from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality.entity.entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    # download the data file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file,
            )
            logger.info(f"{filename} downloaded! with the following info: \n{header}")
        else:
            logger.info(f"File already exists")

    # extracting the zip file
    def extract_zip_file(self):
        """Extracts the zip file into the data directory"""

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

