from WasteDetection.pipelines.training_pipeline import TrainPipeline

train_pipeline = TrainPipeline()

ingestion_artifacts = train_pipeline.run_train_pipeline()
print(ingestion_artifacts)