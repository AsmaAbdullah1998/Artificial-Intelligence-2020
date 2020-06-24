import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'


#Video#

#First project!-importing video

#defingn the path of the video
vid_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\BeachVideo.mp4'
#import our video inside() will write the path
cap = cv2.VideoCapture(vid_Path)
#beacuse the video is just a sequcane of images! we will use a while loop to go through each frame one by one 
while True:
    #save the image in variable img and then it will tells us wheather it's successed or not!--success will be a boolen!  true of false
    success, img = cap.read()
    #show the result we will use imshow function as above. first parameter is name of window second is the image
    cv2.imshow("video", img)
    #wainting and if you press q then it will close the video
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
