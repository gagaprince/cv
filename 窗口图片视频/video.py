import cv2
import sys

cap = cv2.VideoCapture(sys.path[0]+"/video.mp4")

while True:
    rel, frame = cap.read()
    cv2.imshow('video',frame)

    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

