# face detection & eye detection
import numpy as np
import cv2

cap = cv2.VideoCapture('assets/webcam.mp4')

#Haar-cascade Detection
    #pretrained classifier - picks specific features & chooses which features match face/eye/any obj
    #looks for indicated face/eye/any object
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


# Image captured as frame from video
while True:
    ret, frame = cap.read() #captures frame(image - numpy array), 

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #min neighbor - 5
    for (x,y,w,h) in faces: #face rectangle - x,y,w,h
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 5) #topleft, bottomright, color, line thickness
        roi_gray = gray[y:y+w, x:x+w] #location of face
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3,5)
        for (ex,ey,ew,eh) in eyes: #eye rectangle - ex,ey,ew,eh
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0),5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()