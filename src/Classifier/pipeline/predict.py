import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model1.h5"))

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        predictions = model.predict(test_image)
        predicted_class_index = np.argmax(predictions, axis=1)[0]
        confidence = float(np.max(predictions)) * 100  # Highest probability
        probability = confidence  # Same as confidence unless you want another metric

        # Map index to label
        if predicted_class_index == 1:
            predicted_class = "normal"
        else:
            predicted_class = "malignant"

        # Example heatmap (placeholder)
        heatmap_path = "/static/results/heatmap.png"

        return {
            "predicted_class": predicted_class,
            "probability": round(probability, 2),
            "confidence": round(confidence, 2),
            "heatmap": heatmap_path
        }

