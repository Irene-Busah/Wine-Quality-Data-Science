"""
data_validation_pipeline.py
============================

The solution implementation below validates data after the ingestion
"""

# importing the needed libraries
from src.wine_quality.components.data_transformation import DataTransformation
from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality import logger



# defining the data ingestion dataclass
STAGE_NAME = "Data Transformation Stage"

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.data_splitting()


if __name__ == '__main__':
    try:
        logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
        obj = DataTransformationPipeline()
        obj.initiate_data_transformation()
        logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")
    
    except Exception as e:
        logger.exception(e)
        raise e


