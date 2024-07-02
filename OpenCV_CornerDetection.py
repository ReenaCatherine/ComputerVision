# video - corner detection
#shi-tomasi corner detector

import numpy as np
import cv2

img = cv2.imread('assets/chessboard.jpg')
img = cv2.resize(img, (0,0), fx=0.6,fy=0.6)
#change to grayscale before passing on to next step
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#corner detection alg
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
#img, no of corners, min quality, min eucli dist
corners = np.int0(corners) #convert float corners to int
for corner in corners:
    x,y = corner.ravel() #flattens the array by removing brackets
    cv2.circle(img, (x,y), 5, (255,0,0), -1)

#drawing line btn corners
for i in range(len(corners)):
    for j in range(i+1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x:int(x), np.random.randint(0,255, size=3))) #[[[0,0,255]]]
        cv2.line(img, corner1, corner2, color, 1)



cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()