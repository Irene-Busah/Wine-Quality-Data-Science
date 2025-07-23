"""
data_ingestion_pipeline.py
============================

The solution implementation below ingests data from the appropriate link
"""

# importing the needed libraries
from src.wine_quality.components.data_ingestion import DataIngestion
from src.wine_quality.config.config import ConfigurationManager
from src.wine_quality import logger



# defining the data ingestion dataclass
STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f"------------ Stage [{STAGE_NAME}] Started ------------")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f"------------ Stage [{STAGE_NAME}] Completed ------------")
    
    except Exception as e:
        logger.exception(e)
        raise e
