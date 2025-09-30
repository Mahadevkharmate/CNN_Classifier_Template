from src.config.configuration import ConfigurationManager
from src.components.stage03_callbacks import PrepareCallbacks
from src.components.stage04_training import Training
from src.logger.logging import logging

STAGE_NAME = "Training"

#This is the main function for the training stage of the pipeline
def main():
    config = ConfigurationManager() #create a ConfigurationManager object
    prepare_callbacks_config = config.get_prepare_callback_config() #get the prepare callbacks configuration
    prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config) #create a PrepareCallbacks object
    callback_list = prepare_callbacks.get_tb_ckpt_callbacks() #get the list of callbacks

    training_config = config.get_training_config() #get the training configuration
    training = Training(config=training_config) #create a Training object
    training.get_base_model() #load the base model
    training.train_valid_generator() #create the train and valid data generators
    training.train(callback_list=callback_list) #train the model with the callbacks

if __name__ == "__main__":
    try:
        logging.info(f">>>>> stage {STAGE_NAME} started <<<<<") #log the start of the stage
        main() #call the main function
        logging.info(f">>>>> stage {STAGE_NAME} completed <<<<<\n\nx==========x") #log the completion of the stage
    except Exception as e:
        logging.exception(e) #log any exceptions that occur
        raise e
