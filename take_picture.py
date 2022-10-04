import cv2
import os
import shutil

class image_viewer():
    
    def __init__(self,IP_adress:str='172.31.71.140',port:str='8080'):
        self.IP_adress = IP_adress
        self.port = port
        self.cap = cv2.VideoCapture('rtsp://%s:%s/h264_ulaw.sdp' %(IP_adress,port)) #IP Camera

    def take_picture(self,args,name: str):
        #cap = cv2.VideoCapture(0) #default camera
        cap=self.cap
        ret, frame = cap.read()
        parent_dir = os.getcwd()
    
            
        frame=cv2.resize(frame, (960, 540)) 
        cv2.imshow('Capturing',frame)
       
    
        path=os.path.join(parent_dir, 'Images')
       
        if os.path.exists(path):
       # removing the file using the os.remove() method
           shutil.rmtree(path)    
       
       # Create the directory
        os.mkdir(path)
        final_path = os.path.join(path, name)
    
        cv2.imwrite(final_path,frame)
        cap.release()
        cv2.destroyAllWindows()
    
    

        
import sys
name = 'canard.png'
pic=image_viewer()
pic.take_picture(sys.argv,name)