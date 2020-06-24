import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'

#Image#--importing images

#Writing the path of the image
img_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
#Reading the image
img = cv2.imread(img_Path) 
#if it's NONE that means there is something Wrong!! be sure of the path PLZ!
print(img) 
#show the image the first paramete is name appears in the window the second paramete is the img
cv2.imshow("BOY", img)
#This code is for waiting it's in milisecond however, zero means inf!
cv2.waitKey(0)
