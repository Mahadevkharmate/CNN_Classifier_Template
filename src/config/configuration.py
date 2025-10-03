from pathlib import Path
from src.utils.utils import read_yaml, create_directory
from src.constants import CONFIG_FILE_PATH,PARAMS_FILE_PATH
from src.entity.config_entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig,
    PrepareCallbacksConfig,
    TrainingConfig,
    EvaluationConfig
)
import os
class ConfigurationManager:
    def __init__(self,config_filepath=CONFIG_FILE_PATH,params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath) #config.yaml file read
        self.params = read_yaml(params_filepath) #params.yaml file read
        create_directory([Path(self.config["artifacts_root"])]) #create artifacts directory

    def get_data_ingestion_config(self) -> DataIngestionConfig: #return type is DataIngestionConfig
        config = self.config["data_ingestion"] #getting data_ingestion section from config.yaml file
        create_directory([Path(config["root_dir"])]) #create root_dir directory of data_ingestion
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config["root_dir"]),
            source_URL=config["source_URL"],
            local_data_file=Path(config["local_data_file"]),
            unzip_dir=Path(config["unzip_dir"])
        )
        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config["prepare_base_model"]
        params = self.params
        create_directory([Path(config["root_dir"])])
        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir = Path(config["root_dir"]),
            base_model_path = Path(config["base_model_path"]),
            updated_base_model_path = Path(config["updated_base_model_path"]),
            params_image_size = params["IMAGE_SIZE"],
            params_learning_rate = params["LEARNING_RATE"],
            params_include_top = params["INCLUDE_TOP"],
            params_weights = params["WEIGHTS"],
            params_classes = params["CLASSES"]
        )
        return prepare_base_model_config


    def get_prepare_callback_config(self) -> PrepareCallbacksConfig:
        config = self.config["prepare_callbacks"]
        model_ckpt_dir = os.path.dirname(config.checkpoint_model_filepath)
        create_directory([
            Path(model_ckpt_dir),
            Path(config.tensorboard_root_log_dir)
        ])

        prepare_callback_config = PrepareCallbacksConfig(
            root_dir=Path(config["root_dir"]),
            tensorboard_root_log_dir=Path(config["tensorboard_root_log_dir"]),
            checkpoint_model_filepath=Path(config["checkpoint_model_filepath"])
        )

        return prepare_callback_config

    def get_training_config(self) -> TrainingConfig:
        config = self.config["training"] #getting training section from config.yaml file
        params = self.params #getting all parameters from params.yaml file
        create_directory([Path(config["root_dir"])]) #create root_dir directory of training
        prepare_base_model = self.config["prepare_base_model"] #getting prepare_base_model section from config.yaml file
        training_data = os.path.join(self.config["data_ingestion"]["unzip_dir"],"PetImages") #path where data is unzipped
        training_config = TrainingConfig( 
            root_dir=Path(config["root_dir"]),
            trained_model_path=Path(config["trained_model_path"]),
            updated_base_model_path=Path(prepare_base_model["updated_base_model_path"]),
            training_data=Path(training_data),
            params_epochs=params["EPOCHS"],
            params_batch_size=params["BATCH_SIZE"],
            params_is_augmentation=params["AUGMENTATION"],
            params_image_size=params["IMAGE_SIZE"]
        )   #prepare TrainingConfig dataclass object
        return training_config

    def get_validation_config(self) -> EvaluationConfig:
        trained_model = self.config["training"] #getting training section from config.yaml file
        eval_config = self.config["evaluation"] #getting evaluation section from config.yaml file

        eval_config = EvaluationConfig(
            path_of_model=Path(trained_model["trained_model_path"]),
            training_data=Path(eval_config["training_data"]),
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE
        )
        
        return eval_config