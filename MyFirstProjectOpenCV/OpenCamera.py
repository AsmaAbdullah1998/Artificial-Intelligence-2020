import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'

#Second Project-open the camera of the laptop!

#write the id of our camera in () zero for laptop connected zero will use the defult webcam
cap = cv2.VideoCapture(0) 
#we want it for specific size widht
cap.set(3,640)
#define the height 
cap.set(4, 480)
#change the brightness 
cap.set(10,100)
#The rest of the code is the same as above!
while True:
    #save the image in variable img and then it will tells us wheather it's successed or not!--success will be a boolen!  true of false
    success, img = cap.read()
    #show the result we will use imshow function as above. first parameter is name of window second is the image
    cv2.imshow("video", img)
    #wainting and if you press q then it will close the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
         break 