"""
model_evaluation_pipeline.py
============================

The solution implementation below evaluate the model
"""

# importing the needed libraries
from src.wine_quality.components.model_evaluation import ModelEvaluation
from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality import logger



# defining the data ingestion dataclass
STAGE_NAME = "Model Evaluation Stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_to_mlflow()


if __name__ == '__main__':
    try:
        logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
        obj = ModelEvaluationPipeline()
        obj.initiate_model_evaluation()
        logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")
    
    except Exception as e:
        logger.exception(e)
        raise e


