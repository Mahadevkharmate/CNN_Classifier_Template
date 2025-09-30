from src.logger.logging import logging
from src.config.configuration import ConfigurationManager
from src.components.stage05_evaluation import Evaluation

STAGE_NAME = "Evaluation"

#This is the main function for the evaluation stage of the pipeline
def main():
    config = ConfigurationManager() #create a ConfigurationManager object
    eval_config = config.get_validation_config() #get the evaluation configuration
    eval = Evaluation(config=eval_config) #create an Evaluation object
    eval.evaluation() #evaluate the model
    eval.save_score() #save the evaluation scores


if __name__ == "__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<") #log the start of the stage
        main() #call the main function
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x") #log the completion of the stage
    except Exception as e:
        logging.exception(e) #log any exceptions that occur
        raise e