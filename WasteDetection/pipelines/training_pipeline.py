import os
import sys
from WasteDetection.logger import logging
from WasteDetection.exception import CustomException
from WasteDetection.entity.artifacts_entity import DataIngestionArtifact

from WasteDetection.components.data_ingestion import DataIngestion
from WasteDetection.entity.config_entity import DataIngestionConfig


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        
        
    def start_data_ingestion(self):
        try : 
            logging.info("Started data ingestion pipeline method of TrainPipeline class...")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    def run_train_pipeline(self):
        try : 
            data_ingestion_artifact = self.start_data_ingestion()
            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys)
            

    