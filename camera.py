#!/usr/bin/python

import  cv2
# All functions of cv2 that is in opencv model
import random

# now starting cam
cap=cv2.VideoCapture(0)

while   cap.isOpened() :
	print  "camera is working"
	status,frame=cap.read()
	bwimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	cv2.rectangle(frame,(100,100),(200,200),(0,0,255),2)
	# *Deciding font type
	font=cv2.FONT_HERSHEY_SIMPLEX
	# *To put some text in that image:-
	#	data,text,starting point,font-type,size,color,line type(width)
	cv2.putText(frame,"BOSS",(100,100),font,3,(100,23,200),lineType=cv2.LINE_AA)
	cv2.imshow("camera1",frame)
	x=random.random()
	y=str(x)[2:6]
	cv2.imwrite('suharsh'+y+'.jpg',frame)
	#cv2.imshow("camera2",bwimg)
	if   cv2.waitKey(1)  &  0xFF  == ord('q')  :
		break  

cv2.destroyAllWindows()
cap.release()
