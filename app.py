import os
import sys
import yaml
from pathlib import Path
import pathlib 
import platform
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from WasteDetection.exception import CustomException
from WasteDetection.logger import logging
from WasteDetection.utils.main_utils import encodeImageIntoBase64, decodeImage

from WasteDetection.constant.application import APP_PORT, APP_HOST
from WasteDetection.pipelines.training_pipeline import TrainPipeline

app = Flask(__name__)

plt = platform.system()

if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

class ClientApp:
    def __init__(self):
        self.filename = "input_image.jpg"
        
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/train")
def train():
    train_pipeline = TrainPipeline()
    model_trainer_artifacts = train_pipeline.run_train_pipeline()
    return "Training has completed successfully"

@app.route("/predict", methods=['GET', 'POST'])
def predict():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        # Ensure paths are correct and OS-independent
        os.system("cd yolov5 && python detect.py --weights best.pt --img 416 --conf 0.5 --source ../data/input_image.jpg")
        print("current working dir:", os.getcwd())
        
        base64_image = encodeImageIntoBase64("yolov5/runs/detect/exp/input_image.jpg")
        result = {"image": base64_image.decode('utf-8')}
        print(os.getcwd())
        # Clean up after processing
        os.system("rm -rf yolov5/runs")

    except ValueError as val:
        return Response("Value not found inside json data")
    except KeyError:
        return Response("Key not found inside json data")
    except Exception as e:
        print(e)
        result = "invalid_input"

    return jsonify(result)

@app.route("/live", methods=['GET'])
def predict_live():
    try:
        # Ensure URL is correct and accessible from your environment
        os.system("cd yolov5 && python detect.py --weights best.pt --img 416 --conf 0.7 --source http://192.168.1.11:8080/video")
        
        # Clean up after processing
        os.system("rm -rf yolov5/runs")
        return "camera starting"
    
    except ValueError as val:
        return Response("Value not found inside json data")

if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, 
            port=APP_PORT, 
            debug=True)
