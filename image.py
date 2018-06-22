#!/usr/bin/python2

import cv2
# all functions of cv2 that is opencv model

import image

# reading image:
#	image name,image features
# 			loading image

# we can write	cv2.IMREAD_COLOR instead of 1
# we can write cv2.IMREAD_BGR2GRAY instead of 0
# we can write cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("dog.jpg",1)
img1=cv2.imread("dog.jpg",0)
img2=cv2.imread("dog.jpg",-1)

# checking rows and columns
print img.shape
print img1.shape
print img2.shape

# to show original data of image
print img

# to display that image
cv2.imshow("windowname",img)
cv2.imshow("bwimg",img1)
cv2.imshow("newok",img2)

# save black and white (GRAY) image
cv2.imwrite("bac.jpg",img1)

# image window holder activate
cv2.waitkey(0)


# waitkey will destroy by using q button
# cv2.destroyAllWindows()



