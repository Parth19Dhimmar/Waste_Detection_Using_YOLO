import os
import sys
import gdown
from zipfile import ZipFile

from WasteDetection.logger import logging
from WasteDetection.exception import CustomException
from WasteDetection.entity.artifacts_entity import DataIngestionArtifact
from WasteDetection.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, data_ingestion_config : DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e, sys)
    

    def download_data(self):
        try:
            dataset_url = self.data_ingestion_config.data_download_url
            zip_download_dir = self.data_ingestion_config.data_ingestion_dir
            os.makedirs(zip_download_dir, exist_ok = True)
            data_file_name = "data.zip"
            zip_file_path = os.path.join(zip_download_dir, data_file_name)
            logging.info("Downloading the data file...")
        
            file_id = dataset_url.split("/")[-2]
            prefix = "https://drive.google.com/uc?/export=download&id="
            gdown.download(prefix + file_id, zip_file_path )
            logging.info("Downloaded the data file...")

            return zip_file_path

        except Exception as e:
            raise CustomException(e, sys)
    
    def unzip_data(self, zip_file_path : str):
        try:
            feature_store_path = self.data_ingestion_config.feature_store_file_path
            os.makedirs(feature_store_path, exist_ok = True)
            with ZipFile(zip_file_path, 'r') as zObject:
                zObject.extractall(path = feature_store_path)
            logging.info("Successfully extracted data from the zip_file...")

            return feature_store_path

        except Exception as e:
            raise CustomException(e, sys)
        

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        try : 
            logging.info("Initiated the data ingestion method...")

            zip_file_path = self.download_data()
            feature_store_path = self.unzip_data(zip_file_path)

            data_ingestion_artifact = DataIngestionArtifact(
                data_zip_file_path = zip_file_path,
                feature_store_path = feature_store_path
            )

            logging.info(f"Data_ingestion_artifact : {data_ingestion_artifact}...")

            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e, sys)