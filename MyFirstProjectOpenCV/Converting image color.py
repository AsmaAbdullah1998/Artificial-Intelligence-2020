import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'


#Basic funtions in OpenCV 

#Image#--importing images

#Writing the path of the image
img_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
#Reading the image
img = cv2.imread(img_Path) 
#if it's NONE that means there is something Wrong!! be sure of the path PLZ!
print(img) 
#show the image the first paramete is name appears in the window the second paramete is the img
cv2.imshow("Befor", img)

#Converting the color of the image!-WOW-
#the path of the image
img_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
#Reading the image
img = cv2.imread(img_Path)
#defining the Gray image this convert the image into diffrent color! first parametr is for the image the second is the color
#in OpenCv we use BGR instead of RBG!
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# show the imagethe first parameter is for the name of the window, the second is for the image
cv2.imshow("Gray Image", imgGray)
#waiting....
cv2.waitKey(0)