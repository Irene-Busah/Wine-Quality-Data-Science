from src.wine_quality import logger
from src.wine_quality.pipeline.data_ingestion_pipeline import DataIngestionTrainingPipeline


logger.info("Welcome to our Custom Logging for the End-to-end Data Science Project")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
    obj = DataIngestionTrainingPipeline()
    obj.initiate_data_ingestion()
    logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")

except Exception as e:
    logger.exception(e)
    raise e