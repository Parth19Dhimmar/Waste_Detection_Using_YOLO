import os
import sys
import shutil
from WasteDetection.exception import CustomException
from WasteDetection.logger import logging
from WasteDetection.entity.artifacts_entity import DataIngestionArtifact, DataValidationArtifact
from WasteDetection.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, data_ingestion_artifact : DataIngestionArtifact, data_validation_config : DataValidationConfig ):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
        except Exception as e:
            raise CustomException(e, sys)
        
    def validate_data(self):
        try:
            validation_status = False
            logging.info("Checking feature store path for required files")
            all_files = os.listdir(self.data_ingestion_artifact.feature_store_path)
            for file in all_files:
                if file not in self.data_validation_config.required_file_list:
                    validation_status = False
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok = True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as file:
                        file.write(f"validation_status : {validation_status}")
                else:
                    validation_status = True
                    os.makedirs(self.data_validation_config.data_validation_dir, exist_ok = True)
                    with open(self.data_validation_config.valid_status_file_dir, 'w') as file:
                        file.write(f"validation_status : {validation_status}")   

            return validation_status     

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_validation(self) -> DataValidationArtifact:
        try:
            logging.info("initiating data validation, entering validate data method...")

            status = self.validate_data()    
            data_validation_artifact = DataValidationArtifact(validation_status = status)

            logging.info(f"Exited the validate data method, validation_status : {status}")
            logging.info(f"Data validatiopn artifact : {data_validation_artifact}")

            if status:
                shutil.copy(self.data_ingestion_artifact.data_zip_file_path, os.getcwd())

            return data_validation_artifact
    
        except Exception as e:
            raise CustomException(e, sys)

