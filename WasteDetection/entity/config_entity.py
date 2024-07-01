import os
from datetime import datetime
from dataclasses import dataclass
from WasteDetection.constant.training_pipeline import *

@dataclass
class TrainingPipelineConfig:
    artifacts_dir : str = ARTIFACTS_DIR

training_pipeline_config = TrainingPipelineConfig()

@dataclass
class DataIngestionConfig:
    
    data_ingestion_dir = os.path.join(training_pipeline_config.artifacts_dir, DATA_INGESTION_DIR_NAME)

    feature_store_file_path = os.path.join(data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR)

    data_download_url = DATA_DOWNLOAD_URL


@dataclass
class DataValidationConfig:

    data_validation_dir = os.path.join(training_pipeline_config.artifacts_dir, DATA_VALIDATION_DIR )

    valid_status_file_dir = os.path.join(data_validation_dir, VALID_STATUS_FILE_DIR)

    required_file_list = REQUIRED_FILE_LIST

@dataclass
class ModelTrainerConfig:

    model_trainer_dir = os.path.join(training_pipeline_config.artifacts_dir, MODEL_TRAINER_DIR)

    model_weight_name = MODEL_TRAINER_PRETRAINED_WEIGHT_NAME

    model_epochs = MODEL_TRAINER_NO_EPOCHS

    model_batch_size = MODEL_TRAINER_BATCH_SIZE
