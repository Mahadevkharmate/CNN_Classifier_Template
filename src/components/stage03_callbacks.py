import os
from src.entity.config_entity import PrepareCallbacksConfig
import tensorflow as tf
import time
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping

class PrepareCallbacks:
    def __init__(self, config: PrepareCallbacksConfig):
        self.config = config

    @property
    def _create_tb_callbacks(self):
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tb_running_log_dir = os.path.join(self.config.tensorboard_root_log_dir,
                                           f"tensorborad_logs_at_{timestamp}"
                                           )
        tb_callback = tf.keras.callbacks.TensorBoard(log_dir=tb_running_log_dir)
        return tb_callback
    
    @property
    def _create_ckpt_callbacks(self):
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only =True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]
    
    # Additional callback for early stopping
    def get_callbacks(self): 
        checkpoint_cb = ModelCheckpoint(
            filepath = self.config.checkpoint_model_filepath,
            save_best_only = True,
            monitor = "val_loss",
            mode = "min",
            save_weights_only = False
        ) # ModelCheckpoint callback to save the best model based on validation loss
        early_stopping_cb = EarlyStopping(
            monitor = "val_loss",
            patience = 5,
            mode = "min",
            restore_best_weights = True
        )# EarlyStopping callback to stop training if validation loss doesn't improve for 5 epochs
        return [checkpoint_cb, early_stopping_cb]