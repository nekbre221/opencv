#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 09:45:53 2023

@author: nekui-tiefang
"""

import cv2
import numpy as np

# Charger l'image en niveaux de gris
img = cv2.imread("image.jpg", 0)

# Appliquer la binarisation
thresh = 100
_, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

# Afficher les résultats
cv2.imshow("Originale", img)
cv2.imshow("Custom", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Appliquer le seuillage adaptatif
adaptive_thresh200 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 201, 1)
adaptive_thresh100 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 1)
adaptive_thresh50 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, 1)
adaptive_thresh10 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 19, 1)


cv2.imshow("Originale", img)
cv2.imshow("Adaptive Threshold_block=200", adaptive_thresh200)
cv2.imshow("Adaptive Threshold_block=100", adaptive_thresh100)
cv2.imshow("Adaptive Threshold_block=51", adaptive_thresh50)
cv2.imshow("Adaptive Threshold_block=11", adaptive_thresh10)

cv2.waitKey(0)
cv2.destroyAllWindows()

































