#!/usr/bin/python2

import cv2
# All functions of cv2 that is opencv model

# To start web or external web camera
# 	camera number decide which camera we want to use (0) as inetrnal webcam,(1) as external webcam

capture=cv2.VideoCapture(0)

if capture.isOpened() :
	print "camera is ready to take picture"
#	current camera data ,after frame take camera status
	frame,status=capture.read()
	cv2.imshow("framee1",frame)
	cv2.waitkey(0)
	capture.release()
else :
	print "check your camera drivers with OS"

#dir(cam)

#cam.isOpened()
#	True will show for&if camera start
#	False will show for&if camera not working

#cam.release()
#	to release the capturing mode


