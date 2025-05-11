import os
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from src.Classifier.entity.config_entity import PrepareBaseModelConfig


# Main class that prepares and updates the base model
class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.applications.EfficientNetB0(
            input_shape=tuple(self.config.params_image_size),
            weights=self.config.params_weights,
            include_top=self.config.params_include_top
        )
        self.save_model(path=self.config.base_model_path, model=self.model)

    def update_base_model(self):
        # Make all layers trainable
        for layer in self.model.layers:
            layer.trainable = True

        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            learning_rate=self.config.params_learning_rate
        )
        self.save_model(path=self.config.updated_base_model_path, model=self.full_model)

    @staticmethod
    def _prepare_full_model(model, classes, learning_rate):
        x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
        x = tf.keras.layers.Dense(128, activation='relu')(x)
        x = tf.keras.layers.Dropout(0.5)(x)
        output = tf.keras.layers.Dense(classes, activation='softmax')(x)

        full_model = tf.keras.models.Model(inputs=model.input, outputs=output)

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=['accuracy']
        )

        full_model.summary()
        return full_model

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)
