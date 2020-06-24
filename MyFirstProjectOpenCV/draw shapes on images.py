import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'

#draw lines, rectangle, circles

#first we will create a matrix full of zero! -- zero means black by using np
img = np.zeros((512, 512,3),np.uint8)
#cheack the dimension of the image
print(img.shape)
#show the black image!
cv2.imshow("black image", img)

#color the complete image
img[:]=(255,0,0)
#show the image
cv2.imshow("blue image", img)

#first we will create a matrix full of zero! -- zero means black by using np
img = np.zeros((512, 512,3),np.uint8)
#create lines--defining the starting and the ending point of the line and the color and the thickness! (img, starting point, ending point, color, thickness)
cv2.line(img, (0,0),(300,300),(0,255,0),3)
#show the image 
cv2.imshow("line in the image", img)
#waiting...All the image together
cv2.waitKey(0)
