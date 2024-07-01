from WasteDetection.pipelines.training_pipeline import TrainPipeline

train_pipeline = TrainPipeline()

validation_artifacts = train_pipeline.run_train_pipeline()
print(validation_artifacts)