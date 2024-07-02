#  cameras - webcam - Colors / color detection
# BGR to HSV
import numpy as np
import cv2

cap = cv2.VideoCapture('assets/webcam.mp4')

# Image captured as frame from video
while True:
    ret, frame = cap.read() #captures frame(image - numpy array), 
    width = int(cap.get(3)) #gives width ppr of frame
    height = int(cap.get(4)) #gives height

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([90,50,50]) #lightblue
    upper_blue = np.array([130,255,255]) #darkblue

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #returns only blue pixels - 0s and 1s
    
    result = cv2.bitwise_and(frame, frame, mask=mask) #and gate logic

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'): #ord - ordinal val - ascii 
        break #keypressed within 1ms - ascii code of alph



cap.release() #release cam resource - other sw can use
cv2.destroyAllWindows()

# cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) - expcts something with shape
## how to convert a color 
# BGR_color = np.array([[[255,0,0]]])
# x = cv2.cvtColor(BGR_color, cv2.COLOR_BGR2HSV)
# x[0][0] --> gives one pixel