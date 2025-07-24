"""
model_training.py
==================

The file implements the model training class
"""


# importing the necessary libraries
from src.wine_quality.entity.entity import ModelTrainingConfig
import pandas as pd
from sklearn.linear_model import ElasticNet
import joblib
import os


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # extracting the target and depending variables
        x_train = train_data.drop([self.config.target_column], axis=1)
        x_test = test_data.drop([self.config.target_column], axis=1)

        y_train = train_data[[self.config.target_column]]
        y_test = test_data[[self.config.target_column]]

        # training the model
        linear_model = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

        # fitting the model
        linear_model.fit(x_train, y_train)

        joblib.dump(linear_model, os.path.join(self.config.root_dir, self.config.model_name))


