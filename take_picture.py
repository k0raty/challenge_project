import cv2
import os
import shutil
cap = cv2.VideoCapture('rtsp://172.31.71.140:8080/h264_ulaw.sdp') #IP Camera

def take_picture(args,name: str):
    #cap = cv2.VideoCapture(0) #default camera
    ret, frame = cap.read()
    parent_dir = os.getcwd()

   # while(True):
        
    frame=cv2.resize(frame, (960, 540)) 
    cv2.imshow('Capturing',frame)
   
#       if cv2.waitKey(1) & 0xFF == ord('y'): #save on pressing 'y' 

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
take_picture(sys.argv,name)