#!/usr/bin/env python
# coding: utf-8

# In[2]:


import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import cv2
from PIL import Image
import random as rd


# In[8]:


import sklearn as sk


# In[9]:


def double_conv_block(x,n_filters):
    
    x=tf.keras.layers.Conv2D(n_filters,3,padding="same",activation="relu",kernel_initializer="he_normal")(x)
    x=tf.keras.layers.Conv2D(n_filters,3,padding="same",activation="relu",kernel_initializer="he_normal")(x)
    return x
     

def downsample_block(x,n_filters):
    f=double_conv_block(x,n_filters)
    p=tf.keras.layers.MaxPool2D(2)(f)
    p=tf.keras.layers.Dropout(0.3)(p)
    return f,p
def upsample_block(x,conv_features,n_filters):
    
    
    
    x=tf.keras.layers.Conv2DTranspose(n_filters,3,2,padding="same")(x)
    x=tf.keras.layers.concatenate([x,conv_features])
    x=tf.keras.layers.Dropout(0.3)(x)
    x=double_conv_block(x,n_filters)
    return x
    
def build_unet_model():

    inputs=tf.keras.layers.Input(shape=(128,128,3))
  # encoder: contracting path - downsample
    f1,p1=downsample_block(inputs,64)
    f2,p2=downsample_block(p1,128)
    f3,p3=downsample_block(p2,256)
    f4,p4=downsample_block(p3,512)
    bottleneck=double_conv_block(p4,1024)

  # decoder: expanding path - upsample
    u6=upsample_block(bottleneck,f4,512)
    u7=upsample_block(u6,f3,256)
    u8=upsample_block(u7,f2,128)
    u9=upsample_block(u8,f1,64)

    outputs=tf.keras.layers.Conv2D(1,1,padding="same",activation = "sigmoid")(u9)
    print(outputs.shape)

    unet_model = tf.keras.Model(inputs, outputs, name="U-Net")
    return unet_model


# In[10]:


path="E:\Walls"


# In[11]:


model = build_unet_model()


# In[12]:


model


# In[15]:


model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[ ]:




