#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 08:18:26 2023

@author: nekui-tiefang
"""
import numpy as np
import cv2

#####recuperer une image avec opencv
img=cv2.imread("image.jpg")
cv2.namedWindow("Image")
cv2.imshow("Image", img)
cv2.moveWindow("Image", 0, 0)
cv2.waitKey(0)
cv2.imwrite("image_opencv.png", img)
cv2.destroyAllWindows()


############## Capture vidéo
import numpy as np
import cv2 
cap=cv2.VideoCapture("Cars.mp4")

while(True):
    ret, frame=cap.read()
    
    frame=cv2.resize(frame, (0,0),fx=0.5,fy=0.5)
    cv2.imshow("image", frame)
    cv2.moveWindow("image", 0, 0)
    
    ch=cv2.waitKey(1)
    if ch & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()    














