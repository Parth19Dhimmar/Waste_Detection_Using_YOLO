import sys
import os
import yaml
import base64

from WasteDetection.logger import logging
from WasteDetection.exception import CustomException

def read_yaml_file(file_path : str):
    try:
        with open(file_path, 'rb') as yaml_file:
            logging.info("Read yaml file successfully!")
            data = yaml.safe_load(yaml_file)
    except Exception as e:
        raise CustomException(e, sys)
    
def save_yaml_file(file_path : str, content : object, replace : bool = False) -> None:
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
            
            os.makedirs(os.path.dirname(file_path), exist_ok = True)

            with open(file_path, 'wb') as yaml_file:
                yaml.dump(content, yaml_file)
                logging.info("Saved yaml file successfully")

    except Exception as e:
        raise CustomException(e, sys)
    

def encodeImageIntoBase64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read())

def decodeImage(encoded_img_string, filename):
    decoded_string = base64.b64decode(encoded_img_string)
    with open("./data/" + filename, 'wb') as image_file:
        image_file.write(decoded_string)
        image_file.close()