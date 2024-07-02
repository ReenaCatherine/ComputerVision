#  cameras - webcam - Drawing shapes / text
import numpy as np
import cv2

cap = cv2.VideoCapture('assets/webcam.mp4')

# Image captured as frame from video
while True:
    ret, frame = cap.read() #captures frame(image - numpy array), 
    width = int(cap.get(3)) #gives width ppr of frame
    height = int(cap.get(4)) #gives height

    #line - # sourceimg, starting position, ending position, color, line thickness
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    img = cv2.line(img, (0,height), (width, 0), (0,255,0), 5) #for diagonal
    img = cv2.rectangle(img, (100,100), (200,200),(128,128,128), 5) # -1 in place of 5 -filled rect
    #circle - sourceimg, centre position, radius, color, line thickness
    img = cv2.circle(img, (300,300), 60, (0,0,255), -1)
    #text - img, text, center position, font, font scale, color, thickness, linetype
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Reena is ML Engineer', (20, height-10), font, 1, (0,0,0), 5, cv2.LINE_AA)
    
    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): #ord - ordinal val - ascii 
        break #keypressed within 1ms - ascii code of alph



cap.release() #release cam resource - other sw can use
cv2.destroyAllWindows()