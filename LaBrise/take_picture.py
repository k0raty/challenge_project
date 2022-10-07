import cv2
import os
import shutil
import sys

class image_viewer():
    
    def __init__(self,IP_adress:str='192.168.43.1',port:str='8080'):
        self.IP_adress = IP_adress
        self.port = port
        #self.cap = cv2.VideoCapture(0) #IP Camera
        self.cap = cv2.VideoCapture('rtsp://%s:%s/h264_ulaw.sdp' %(IP_adress,port)) #IP Camera

        parent_dir = 'C:\RoboDK\Python\LaBrise'
        self.path=os.path.join(parent_dir, 'Images')

        if os.path.exists(self.path): # removing the file using the os.remove() method
           shutil.rmtree(self.path)
        
        # Create the directory
        os.mkdir(self.path)

    def take_picture(self,args,name: str):
        cap=self.cap
        ret, frame = cap.read()

        #frame=cv2.resize(frame, (960, 540)) 
        #cv2.imshow('Capturing',frame)
       
        final_path = os.path.join(self.path, name)
    
        cv2.imwrite(final_path,frame)
        #cap.release()
        cv2.destroyAllWindows()