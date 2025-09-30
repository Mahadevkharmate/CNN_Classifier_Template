from src.logger.logging import logging
from src.config.configuration import ConfigurationManager
from src.components.stage02_prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare Base Model Stage"
def main():
    try:
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config = prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
        logging.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e
    
if __name__ == "__main__":
    try:
        logging.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<")
        main()
        logging.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x")
    except Exception as e:
        logging.exception(e)
        raise e 