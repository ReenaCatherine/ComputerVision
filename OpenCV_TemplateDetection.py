#object detection
#template image close to actual size of actual obj in base image
# if matching not happening/not able to view, resize the original img & template img

import numpy as np
import cv2

img = cv2.resize(cv2.imread('assets/soccer.jpg', 0),(0,0),fx=0.8,fy=0.8)
template = cv2.resize(cv2.imread('assets/shoe.png', 0),(0,0),fx=0.8,fy=0.8) # ,0 makes image grayscale
h,w = template.shape #height,width,channels - bgr; height, width - grayscale

#methods for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2, template, method) #convolution step - 2d array
    #(W-w+1, H-h+1) position --> W-width of base img, w-width of template img
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 