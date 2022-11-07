## Homework - Luminance Image Processor
## COMP 350 
## by Sabrina Galban
## This python program creates a luminance image of the read in image
## by creating a mask for the blue and green HSV values and applying 
## it to the image.

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('message.png')

img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

lower_HSV = np.array([50,100,50])
upper_HSV = np.array([130,255,255])

mask = cv2.inRange(img_hsv, lower_HSV, upper_HSV)

img_bgr_masked = cv2.bitwise_and(img_bgr, img_bgr, mask = mask)

img_rgb = cv2.cvtColor(img_bgr_masked, cv2.COLOR_BGR2HSV)

plt.imshow(img_rgb), plt.axis("off")
plt.show()