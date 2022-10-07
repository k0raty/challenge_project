#!/usr/bin/env python
# coding: utf-8



#Imports 
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pandas as pd
from pathlib import Path
import shutil




class filter_picture():
    
    def __init__(self, model_PATH :str = "../models/model_filtre.h5",picture_PATH :str = 'Images'):
       self.model_path=model_PATH
       self.picture_path=picture_PATH
       self.model = load_model(self.model_path)
        
        
    
    def generate_df(self):
        image_dir=Path(self.picture_path)
        filepaths = pd.Series(list(image_dir.glob(r'*.jpg')), name='Filepath').astype(str)
        #labels = pd.Series(label, name='Label', index=filepaths.index)
        df=filepaths
        #df = pd.concat([filepaths, labels], axis=1)
        return df
    
    def get_filtered_pictures(self):
        
        parent_dir = os.getcwd()
        path=os.path.join(parent_dir, 'Filtred_pictures')
       
        if os.path.exists(path):
       # removing the file using the os.remove() method
           shutil.rmtree(path)    
       
       # Create the directory
        os.mkdir(path)
    
        
        df=self.generate_df()
        
        
        
        for i in range(len(df)):
            
            fig, (ax1,ax2) = plt.subplots(1, 2)
            img_path =df[i]
            img= cv2.imread(img_path, cv2.IMREAD_COLOR)
            print(img.shape)
            img = cv2.resize(img, (128, 128), interpolation=cv2.INTER_AREA)
            print(img.shape)
            img = tf.cast(img, tf.float32) / 255.0
       #☺     plt.subplot(1,2,1)
         #   plt.axis(False)
            ax1.set_title("Original Image", fontweight="bold")
            ax1.imshow(img)
           # plt.subplot(1,2,2)
           # plt.axis(False)
            ax2.set_title("Predicted Mask", fontweight="bold")
            img = np.expand_dims(img,axis=0)
            ax2.imshow(self.model.predict(img)[0,:,:,:]) 
            plt.show() 
            fig.savefig('Filtred_pictures/image_%d'%i)


# In[ ]:




