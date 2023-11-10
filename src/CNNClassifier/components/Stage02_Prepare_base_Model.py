from CNNClassifier.logger import logger
import os,sys
from pathlib import Path
from CNNClassifier.entity.config_entity import PrepareBaseModelConfig
import tensorflow as tf
from CNNClassifier.utils.utils import save_model

class PrepareBaseModel:
    def __init__(self,config:PrepareBaseModelConfig):
        self.config= config

    def get_base_model(self):
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.param_image_size,
            weights= self.config.param_weight,
            include_top= self.config.param_include_top
        )
        save_model(path = self.config.base_model_path, model= self.model)

    @staticmethod
    def prepare_full_model(model, freeze_all, classes, freeze_till, learning_rate):
        if freeze_all:
            for layer in model.layers:
                model.trainable = False
        elif (freeze_till is not None) and (freeze_till > 0):
            for layer in model.layers[: -freeze_till]:
                model.trainable = False
        
        flatten = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes,
                              activation='softmax',
                            )(flatten)
        
        full_model = tf.keras.models.Model(
            inputs= model.input,
            outputs= prediction

        )

        full_model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
            loss=tf.keras.losses.categorical_crossentropy,
            metrics=["accuracy"]
        )

        full_model.summary()
        return full_model

    def update_base_model(self) :
        self.full_model = self.prepare_full_model(
            model=self.model,
            classes= self.config.param_class,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )

        save_model(path =self.config.updated_base_model_path, model = self.full_model )

    # @staticmethod
    # def save_model(path: Path, model: tf.keras.Model):
    #     model.save(path)