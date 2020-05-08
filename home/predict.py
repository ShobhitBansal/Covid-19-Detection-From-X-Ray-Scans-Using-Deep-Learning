import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 

import numpy  as np
from keras.preprocessing import image
from pathlib import Path
from keras.models import load_model

folder_name = input("\nEnter the name of the input folder: ")
p = Path(folder_name)

img_name = []
data = []
cnt = 0
for imgs in p.glob("*"):
    name = str(imgs).split("\\")[-1]
    img_name.append(name)
    img = image.load_img(imgs,target_size=(224,224))
    img = image.img_to_array(img)
    data.append(img)

print("\nNumber of images: ",len(data))
Xtest = np.array(data)

model = load_model("./model/covid_model.hdf5")
output = model.predict(Xtest)

result = []
output = output.astype('int')
for i in range(output.shape[0]):
    if output[i]>0.5:
        result.append('Normal')
    else:
        result.append('Covid')

for i in range(len(img_name)):
    print("\n",img_name[i]," : ",result[i])