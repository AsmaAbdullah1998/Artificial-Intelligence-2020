import cv2
print("Package Imported")


#Image#--importing images

# #Writing the path of the image
# img_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\boy.jpg'
# #Reading the image
# img = cv2.imread(img_Path) 
# #if it's NONE that means there is something Wrong!! be sure of the path PLZ!
# print(img) 
# #show the image the first paramete is name appears in the window the second paramete is the img
# cv2.imshow("BOY", img)
# #This code is for waiting it's in milisecond however, zero means inf!
# cv2.waitKey(0)



#Video#

#First project!-importing video

# #defingn the path of the video
# vid_Path = r'C:\Users\EngSa\OneDrive\Desktop\MyGithub\Path3\MyFirstProjectOpenCV\BeachVideo.mp4'
# #import our video inside() will write the path
# cap = cv2.VideoCapture(vid_Path)
# #beacuse the video is just a sequcane of images! we will use a while loop to go through each frame one by one 
# while True:
#     #save the image in variable img and then it will tells us wheather it's successed or not!--success will be a boolen!  true of false
#     success, img = cap.read()
#     #show the result we will use imshow function as above. first parameter is name of window second is the image
#     cv2.imshow("video", img)
#     #wainting and if you press q then it will close the video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break 



#Second Project-open the camera of the laptop!

# #write the id of our camera in () zero for laptop connected zero will use the defult webcam
# cap = cv2.VideoCapture(0) 
# #we want it for specific size widht
# cap.set(3,640)
# #define the height 
# cap.set(4, 480)
# #change the brightness 
# cap.set(10,100)
# #The rest of the code is the same as above!
# while True:
#     #save the image in variable img and then it will tells us wheather it's successed or not!--success will be a boolen!  true of false
#     success, img = cap.read()
#     #show the result we will use imshow function as above. first parameter is name of window second is the image
#     cv2.imshow("video", img)
#     #wainting and if you press q then it will close the video
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#          break 


#Basic funtions in OpenCV 

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