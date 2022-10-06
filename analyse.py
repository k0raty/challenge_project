# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:53:52 2022

@author: Marien
"""


import random
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
from tqdm import tqdm

import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
DATADIR="C:\\Users\\Marien\\Desktop\\ImagineMake\\Recuperation_images\\Analyse\\walls"

CATEGORIES = ["Cracked", "Non-cracked"]
trainingdata=[]
def training_data():
    for category in CATEGORIES:  # do dogs and cats
        path = os.path.join(DATADIR,category)  # create path to dogs anpid cats
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                trainingdata.append([img_array,class_num])
            except:
                pass
training_data()
random.shuffle(trainingdata)
X=[]
y=[]
IMG_SIZE=128
for features,label in trainingdata:
    X.append(features)
    y.append(label)


X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
print(X[:5])
y=np.array(y)
print(y[:100])

X_train = X[:10000]
X_train = X_train/255.0
y_train = y[:10000]

model = Sequential()

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:],kernel_regularizer=tf.keras.regularizers.l1(1e-3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:],kernel_regularizer=tf.keras.regularizers.l1(1e-3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3),kernel_regularizer=tf.keras.regularizers.l1(1e-3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(128,kernel_regularizer=tf.keras.regularizers.l1(1e-3)))
model.add(Dense(64,kernel_regularizer=tf.keras.regularizers.l1(1e-3)))


model.add(Dense(1))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
model.add(Activation('sigmoid'))
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=5, validation_split=0.5)
plt.imshow(X[10])
model.predict(X[10])