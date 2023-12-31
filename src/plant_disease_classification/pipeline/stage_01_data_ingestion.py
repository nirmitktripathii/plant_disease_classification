from plant_disease_classification.config.configuration import ConfigurationManager
from plant_disease_classification.components.data_ingestion import DataIngestion
from plant_disease_classification import logger


STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        if data_ingestion_config.flag == "download":
            logger.info(f"Downloading from {data_ingestion_config.source_URL}")
            data_ingestion.download_file()
            data_ingestion.extract_zip_file()
        elif data_ingestion_config.flag == "copy":
            logger.info(f"Copying from {data_ingestion_config.source_dir} to {data_ingestion_config.unzip_dir}")
            data_ingestion.copy_dataset()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e