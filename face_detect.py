#!/usr/bin/python

import cv2

face_data=cv2.CascadeClassifier('haarcascade_frontalcatface.xml')
cap=cv2.VideoCapture(0)

while   cap.isOpened():
            status,frame=cap.read()
            grayimage=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
   
        # showing current image
            cv2.imshow("current image",frame)
            

            if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

cv2.destroyAllWindows()
cap.release()
