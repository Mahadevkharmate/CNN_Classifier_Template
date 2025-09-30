import os
from src.entity.config_entity import PrepareCallbacksConfig
import tensorflow as tf
import time

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
            filepth=self.config.checkpoint_model_filepath,
            save_best_only =True
        )

    def get_tb_ckpt_callbacks(self):
        return [
            self._create_tb_callbacks,
            self._create_ckpt_callbacks
        ]