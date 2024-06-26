import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = "[ %(asctime)s ] - %(message)s")

project_name = "WasteDetection"

list_of_files = [
    ".github/workflows/.gitkeep",
    "data/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/constant/__init__.py",
    f"{project_name}/constant/training_pipeline/__init__.py",
    f"{project_name}/constant/application.py",
    f"{project_name}/entity/config_entity.py",
    f"{project_name}/entity/artifacts_entity.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipelines/__init__.py",
    f"{project_name}/pipelines/training_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    "templates/index.html",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
]

for file_path in list_of_files:
    file_path = Path(file_path)
    
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir != "":
        os.makedirs(file_dir, exist_ok = True)
        logging.info(f"Creating directory -> {file_dir} for the file {file_name}.")

    if (not(os.path.exists(file_name))) or (os.path.getsize(file_name)):
        with open(file_path, 'w') as f:
            pass
            logging.info(f"Creating an empty file {file_name}")

    else:
        logging.info(f"{file_name} is already created.")