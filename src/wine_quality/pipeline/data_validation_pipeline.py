"""
data_validation_pipeline.py
============================

The solution implementation below validates data after the ingestion
"""

# importing the needed libraries
from src.wine_quality.components.data_validation import DataValidation
from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality import logger



# defining the data ingestion dataclass
STAGE_NAME = "Data Validation Stage"

class DataValidationPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
        obj = DataValidationPipeline()
        obj.initiate_data_validation()
        logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")
    
    except Exception as e:
        logger.exception(e)
        raise e


