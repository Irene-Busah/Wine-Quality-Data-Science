"""
model_evaluation.py
==================

The file implements the model evaluation class
"""


# importing the necessary libraries
from src.wine_quality.entity.entity import ModelEvaluationConfig
from src.wine_quality.utils.common import save_json
from src.wine_quality import logger
import joblib
import os
from pathlib import Path

import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from urllib.parse import urlparse

import mlflow



os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/i.busah/Wine-Quality-Data-Science.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="i.busah"
os.environ["MLFLOW_TRACKING_PASSWORD"]="71f1c7abadfdc87c2c2d63a2e5527cea4f09d895"


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    def evaluate_model(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)

        return rmse, mae, r2
    
    def log_to_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]

        # Set MLflow tracking URI and create new experiment if needed
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        experiment_name = "WineQualityExperiment"
        try:
            experiment = mlflow.get_experiment_by_name(experiment_name)
            if experiment is None:
                mlflow.create_experiment(experiment_name)
            mlflow.set_experiment(experiment_name)
        except Exception as e:
            # logger.error(f"Failed to set/create experiment: {e}")
            raise e
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run(run_name='Wine-Quality-Model') as run:
            predicted_qualities = model.predict(x_test)

            (rmse, mae, r2) = self.evaluate_model(y_test, predicted_qualities)

            # saving the metrics
            scores = {"rmse": rmse, "mae": mae, "r2_score": r2}
            save_json(path=Path(self.config.metric_filename), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2)
            
            # Save model locally
            local_model_path = self.config.model_path
            joblib.dump(model, local_model_path)

            # Log model as artifact
            try:
                mlflow.log_artifact(local_model_path, artifact_path="model")
                logger.info(f"Model saved and logged as artifact at {local_model_path}")
            except Exception as e:
                logger.error(f"Failed to log model artifact: {e}")
                raise e

            # Log metrics file as artifact
            mlflow.log_artifact(self.config.metric_filename, artifact_path="metrics")


