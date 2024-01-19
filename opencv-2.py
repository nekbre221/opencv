#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:58:07 2023

@author: nekui-tiefang
"""
import cv2
import numpy as np

###### ajouter un dessin sur une image

img = cv2.imread("image.jpg")
cv2.namedWindow("image")

color_1 = (0,0,255)
color_2 = (0,255,0)
line_width = 3
radius = 80
point_1=(100,100)
point_2=(400,100)
point_3=(600,200)

img =cv2.resize(img,(900,900))
cv2.circle(img, point_1, radius, color_1, line_width)
cv2.rectangle(img, point_2, point_3, color_2, line_width)
cv2.imshow("image", img)
cv2.moveWindow("image", 0, 0)

cv2.imwrite("image_2_opencv.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()


####### ajouter un dessin visé sur un flux video

import numpy as np
import cv2 

cap=cv2.VideoCapture("Cars.mp4")

def pit(event, x, y, flags, param):
    global point_1, point_2, pressed
    if event==cv2.EVENT_LBUTTONDOWN:
        print("pressed",x,y)
        point_1=(x,y)
        point_2=(x+100, y+50)

cv2.namedWindow("image")
cv2.setMouseCallback("image",pit)


while(True):
    ret, frame=cap.read()
    
    frame=cv2.resize(frame, (0,0),fx=0.5,fy=0.5)
    cv2.circle(frame, point_1, radius, color_1, line_width)
    cv2.rectangle(frame, point_2, point_3, color_2, line_width)

    cv2.imshow("image", frame)
    cv2.moveWindow("image", 0, 0)
    
    ch=cv2.waitKey(1)
    if ch & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()     





    































