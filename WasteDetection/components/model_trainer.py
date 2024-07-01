import os
import sys
import yaml
from WasteDetection.exception import CustomException
from WasteDetection.logger import logging

from WasteDetection.utils.main_utils import read_yaml_file, save_yaml_file
from WasteDetection.entity.artifacts_entity import ModelTrainerArtifact
from WasteDetection.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, model_trainer_config : ModelTrainerConfig):
        try : 
            self.model_trainer_config = model_trainer_config
        except Exception as e:
            raise CustomException(e, sys)

    def initiate_model_trainer(self):
        logging.info("unzipping data")
        os.system("unzip data.zip")
        os.system("rm data.zip")

        with open('data.yaml', 'r') as stream:
            num_classes = str(yaml.safe_load(stream)['nc'])

        model_name = self.model_trainer_config.model_weight_name.split(".")[0]

        config = read_yaml_file(f"yolov5/models/{model_name}.yaml")

        config['nc'] = int(num_classes)

        with open(f"yolov5/models/custom_{model_name}.yaml", 'w') as file:
            yaml.dump(config, file)

        logging.info("Saved yaml file changing num_classes...")

        logging.info("Training model on custom data...")
        os.system(f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.model_batch_size} --epochs {self.model_trainer_config.model_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.model_weight_name} --name yolov5s_results  --cache")
        logging.info("Model Training completed succesfully")

        print(os.getcwd())

        os.system("cp yolov5/runs/train/yolov5s_results/weights/best.pt yolov5/")
        os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok = True)

        os.system (f"cp yolov5/runs/train/yolov5s_results/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

        #os.system("rm -rf yolov5/runs")
        os.system("rm -rf train")
        os.system("rm -rf valid")
        os.system("rm -rf data.yaml")

        model_trainer_artifact = ModelTrainerArtifact(trained_model_file_path = "yolov5/best.pt")

        return model_trainer_artifact 
    


