from pathlib import Path
from src.entity.config_entity import TrainingConfig
import os
import tensorflow as tf


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path) #load the updated base model

    def train_valid_generator(self): #create train and valid data generators
        datagenerator_kwargs = dict(rescale=1./255, validation_split=0.2) #rescale the images and split the data into train and valid
        
        dataflow_kwargs = dict(target_size=self.config.params_image_size[:2], 
                               batch_size=self.config.params_batch_size, 
                               interpolation="bilinear") #set the target size, batch size and interpolation method
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(**datagenerator_kwargs) #create a valid data generator

        
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        ) #create a valid data generator from the training data directory


        if self.config.params_is_augmentation: #if augmentation is True
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=20,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            ) #create a train data generator with augmentation
        else:
            train_datagenerator = valid_datagenerator #if augmentation is False, use the valid data generator as the train data generator
    

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        ) #create a train data generator from the training data directory


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model): 
        model.save(path) #save the model to the specified path

    def train(self, callback_list: list): #train the model with the specified callbacks
        self.steps_per_epoch = self.train_generator.samples// self.train_genenrator.batch_size #calculate the steps per epoch
        self.validation_steps = self.valid_generator.samples// self.valid_generator.batch_size #calculate the validation steps

        #fit the model with the train and valid generators, steps per epoch, validation steps, epochs and callbacks
        self.model.fit(
            self.train_generator,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            epochs=self.config.params_epochs,
            callbacks=callback_list
        )
        self.save_model(path=self.config.trained_model_path, 
                        model=self.model) #save the trained model