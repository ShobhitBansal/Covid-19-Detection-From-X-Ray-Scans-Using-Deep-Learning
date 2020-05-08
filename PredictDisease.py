import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import numpy  as np
from keras.preprocessing import image
from pathlib import Path
from tensorflow.keras.models import load_model

model = load_model("./home/model/covid_model.hdf5")
model._make_predict_function()

def predictdisease(image_path):

    img = image.load_img(image_path,target_size=(224,224))
    img = image.img_to_array(img)
    img = img.reshape((1,224,224,3))

    output = model.predict(img)

    if output[0]>0.5:
        result = "Normal"
    else:
        result = "Covid-Infected"

    return result