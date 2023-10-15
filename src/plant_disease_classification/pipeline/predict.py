import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os



class PredictionPipeline:
    def __init__(self,filename):
        self.filename =filename


    
    def predict(self):
        # load model
        model = load_model(os.path.join("data","training", "model.h5"))
        class_list = sorted(os.listdir(os.path.join("data","data_ingestion", "PlantVillage")), key=lambda x: x.lower()) #Creating class list and sorting it case-insensitively for storing corresponding class_labels for predictions purposes
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (224,224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = np.argmax(model.predict(test_image), axis=1)
        # print(result)
        # print(class_list)
        for i,label in enumerate(class_list):
            if result[0] == i:
                prediction = label
                return [{ "image" : prediction}]
        
        