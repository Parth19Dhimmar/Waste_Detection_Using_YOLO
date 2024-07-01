import os
import sys
import yaml
from flask import Flask, request, render_template
from WasteDetection.exception import CustomException
from WasteDetection.logger import logging

from WasteDetection.pipelines.training_pipeline import TrainPipeline

app = Flask(__name__)

app.route("/")
def index():
    return render_template("index.html")

app.route("/predict")
def predict():
    train_pipeline = TrainPipeline()

    model_trainer_artifacts = train_pipeline.run_train_pipeline()
    
    return render_template("index.html")

