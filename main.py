from src.wine_quality import logger
from src.wine_quality.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.wine_quality.pipeline.data_validation_pipeline import DataValidationPipeline
from src.wine_quality.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.wine_quality.pipeline.model_training_pipeline import ModelTrainingPipeline


logger.info("Welcome to our Custom Logging for the End-to-end Data Science Project")


# ====================================== Data Ingestion ======================================
STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e



# ====================================== Data Validation ======================================

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataValidationPipeline()
    obj.initiate_data_validation()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


# ====================================== Data Transformation ======================================

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataTransformationPipeline()
    obj.initiate_data_transformation()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e


# ======================================== Model Training ========================================

STAGE_NAME = "Model Training Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = ModelTrainingPipeline()
    obj.initiate_model_training()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e
