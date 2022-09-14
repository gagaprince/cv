import sys
import cv2
import os

# print(os.getcwd())

cap = cv2.VideoCapture(sys.path[0]+"/meiyan.mp4")

while True:
    rel, frame = cap.read()
    # 高斯模糊
    new_frame = cv2.GaussianBlur(frame, (13, 13), 10,10)
    # 双边模糊
    # new_frame = cv2.bilateralFilter(frame, 21, 50, 80)


    cv2.imshow('video',frame)
    cv2.imshow('video1',new_frame)

    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

