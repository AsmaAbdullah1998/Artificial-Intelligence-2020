import cv2
print("Package Imported")
import numpy as np #when we want to call funtion we just write np.'the name of the funcion'

#To resize the image we need firs to know the current size of our image 

#Write the path of our image
path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
#reading our image
img = cv2.imread(path)
#check the shape of our image--  it gives three numbers (height, width, DGR)
print(img.shape)
#To resize the image, firts we define the image then the width and the height! 
imgResize = cv2.resize(img, (200, 100))
#show the original image the first parameter is the name of the window the second is the image
cv2.imshow("kid", img)
#show the original image the first parameter is the name of the window the second is the image
cv2.imshow("Resized Image", imgResize)
#waiting.........!
cv2.waitKey(0)
