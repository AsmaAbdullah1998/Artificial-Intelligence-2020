import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'


#defining the path of the image
path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
#Reading the image
img = cv2.imread(path)
#show the image
cv2.imshow("kid", img)
#we want to cropp the image by using matrix factionallity--definging the starting/ending point of the width and height-the height first then the width 
imgCropped = img[0:200, 200:500]
#show the cropped image
cv2.imshow("Cropped image", imgCropped)
#waiting...! for both of the two image
cv2.waitKey(0)

