#!/usr/bin/python2

import cv2
# all functions of cv2 that is opencv model
# print dir(cv2)
# import image

# reading image
# 	image name,image features
# loading image

# we can write	cv2.IMREAD_COLOR instead of 1
# we can write  cv2.IMREAD_BGR2GRAY instead of 0
# we can write  cv2.IMREAD_UNCHANGE_COLOR instead of -1

img=cv2.imread("dog.jpg")

# To draw a "Line" in the image:-
# 	imagedata, start point ,end point ,color , line width
cv2.line(img,(0,0),(100,500),(0,0,255),4)

# To draw a "Rectangle" in the image:-
#	data, starting point, ending point, color, line width
cv2.rectangle(img,(20,20),(100,100),(123,34,200),6)

# To fill "Rectangle" with color:-
# cv2.rectangle(img,(20,20),(100,100),(123,34,200),-1)

# TO make "circle" within the image:-
# 	centre, radius, color, circle width
cv2.circle(img,(100,300),80,(12,45,220),3)

# To fill with "Circle" with color:-
# 	centre, radius, color, circle width
# cv2.circle(img,(100,300),80,(12,45,200),-1)


# Putting some text within the Image:-
# *Deciding font type
font=cv2.FONT_HERSHEY_SIMPLEX

# *To put some text in that image:-
#	data,text,starting point,font-type,size,color,line type(width)
#cv2.putText(img,"DOGG",(10,10),font,3,(100,23,200),lineType=cv2.LINE_AA)


cv2.imshow("lineimg",img)
cv2.imwrite("dogline.jpg",img)
cv2.waitkey(0)



