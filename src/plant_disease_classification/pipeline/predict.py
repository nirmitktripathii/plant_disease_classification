import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Persistent model loading for production efficiency
        self.model_path = os.path.join("data", "training", "model.h5")
        if os.path.exists(self.model_path):
            self.model = load_model(self.model_path)
            print(f"Model loaded successfully from {self.model_path}")
        else:
            self.model = None
            print(f"Warning: Model file not found at {self.model_path}. Prediction will fail until model is available.")
        
        # Pre-calculate class labels for faster inference
        village_path = os.path.join("data", "data_ingestion", "PlantVillage")
        if os.path.exists(village_path):
            self.class_list = sorted(os.listdir(village_path), key=lambda x: x.lower())
        else:
            self.class_list = []

    def predict(self):
        if self.model is None:
            # Try to load again if it wasn't found at init (e.g. after training)
            if os.path.exists(self.model_path):
                self.model = load_model(self.model_path)
            else:
                return [{"error": "Model file not found. Please run training first."}]

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Inference using pre-loaded model
        result = np.argmax(self.model.predict(test_image), axis=1)
        
        if len(self.class_list) > 0:
            for i, label in enumerate(self.class_list):
                if result[0] == i:
                    return [{"image": label}]
        
        return [{"error": "Prediction failed or class labels not found."}]
