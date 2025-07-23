"""
data_transformation.py
=====================

This file implements the data transformation for the ML model
"""


from src.wine_quality.entity.entity import DataTransformationConfig
from src.wine_quality import logger
import os
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    # method to split the data into train and test split
    def data_splitting(self):
        data = pd.read_csv(self.config.data_path)

        train, test = train_test_split(data)

        # saving the split data
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Data Splitting Complete")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)

