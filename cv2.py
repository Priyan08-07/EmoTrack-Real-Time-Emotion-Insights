

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import tensorflow as keras
from keras.preprocessing.image import load_img, img_to_array
from keras.preprocessing.image import ImageDataGenerator
from keras.layers import Dense,Input,Dropout,GlobalAveragePooling2D,Flatten,Conv2D,BatchNormization,Activation,MaxPooling2D
from keras.models import Model,Sequential
from keras.optimizers import Adam,SGD,RMSprop

picture_size = 48
folder = "c:\Users\Star\Downloads\data (1)"

dedection = 'helmet'

plt.figure(figsize= (12,12))
for i in range(1, 10, 1):
    plt.subplot(3,3,i)
    img = load_img(folder+"train/"+dedection+"/"+
                  os.listdir(folder + "train/" + dedection)[i], target_size=(picture_size, picture_size))
    plt.imshow(img)   
plt.show()