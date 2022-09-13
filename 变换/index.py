from hashlib import new
import cv2
import os

# print(os.getcwd())

cap = cv2.VideoCapture(os.getcwd()+"/video.mp4")

while True:
    rel, frame = cap.read()

    # 放缩
    # new_frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
    # 翻转
    # new_frame = cv2.flip(frame,1)
    # 旋转
    # new_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    # 仿射
    h, w, ch = frame.shape
    M = cv2.getRotationMatrix2D((w/2,h/2), 30, 0.5)
    new_frame = cv2.warpAffine(frame, M, (w,h))
    
    cv2.imshow('video',new_frame)


    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

