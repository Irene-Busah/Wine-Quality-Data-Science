"""
model_training_pipeline.py
============================

The solution implementation below trains the model
"""

# importing the needed libraries
from src.wine_quality.components.model_training import ModelTraining
from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality import logger



# defining the data ingestion dataclass
STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def initiate_model_training(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model_training = ModelTraining(config=model_training_config)
        model_training.train()


if __name__ == '__main__':
    try:
        logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
        obj = ModelTrainingPipeline()
        obj.initiate_model_training()
        logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")
    
    except Exception as e:
        logger.exception(e)
        raise e


