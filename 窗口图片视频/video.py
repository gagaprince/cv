import cv2
import os

# print(os.getcwd())

cap = cv2.VideoCapture(os.getcwd()+"/video.mp4")

while True:
    rel, frame = cap.read()
    cv2.imshow('video',frame)

    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

