import os
import sys
from WasteDetection.logger import logging
from WasteDetection.exception import CustomException
from WasteDetection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact, ModelTrainerArtifact

from WasteDetection.components.data_ingestion import DataIngestion
from WasteDetection.components.data_validation import DataValidation
from WasteDetection.components.model_trainer import ModelTrainer
from WasteDetection.entity.config_entity import DataIngestionConfig, DataValidationConfig, ModelTrainerConfig


class TrainPipeline:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()
        self.data_validation_config = DataValidationConfig()
        self.model_trainer_config = ModelTrainerConfig()
        
        
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try : 
            logging.info("Started the start_data_ingestion pipeline method of TrainPipeline class...")
            data_ingestion = DataIngestion(data_ingestion_config = self.data_ingestion_config)

            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

            logging.info("Done with the data ingestion process...")
            return data_ingestion_artifact
        
        except Exception as e:
            raise CustomException(e, sys)
    
    
    def start_data_validation(self, data_ingestion_artifact : DataIngestionArtifact)->DataValidationArtifact:
        try:
            logging.info("Started the start_data_validation method of TrainPipeline class...")
            data_validation = DataValidation(data_ingestion_artifact = data_ingestion_artifact,
                                             data_validation_config = self.data_validation_config)

            data_validation_artifact = data_validation.initiate_data_validation()

            logging.info("Done with the data validation process...")

            return data_validation_artifact
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def start_model_trainer(self)-> ModelTrainerArtifact:
        try : 
            logging.info("Started the start_model_trainer method of TrainPipeline class")

            model_trainer = ModelTrainer(model_trainer_config = self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_trainer()

            logging.info("Done with the model trainer process...")

            return model_trainer_artifact
        except Exception as e:
            raise CustomException(e, sys)

    def run_train_pipeline(self):
        try : 
            data_ingestion_artifact = self.start_data_ingestion()

            data_validation_artifact = self.start_data_validation(data_ingestion_artifact = data_ingestion_artifact)
            
            if data_validation_artifact.validation_status == True:
                model_trainer_artifact = self.start_model_trainer()
            else:
                raise Exception("Not all data found or Data is not in correct format.")

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = TrainPipeline()
    obj.run_train_pipeline()
    print("The training has been completed sucessfully!")