import cv2
import os
import numpy as np

# print(os.getcwd())

cap = cv2.VideoCapture(os.getcwd()+"/车辆识别/video.mp4")

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

while True:
    rel, frame = cap.read()
    # 灰度
    cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 去噪
    blur = cv2.GaussianBlur(frame, (3,3),5)
    mask = bgsubmog.apply(blur)

    # 开操作
    open = cv2.morphologyEx(mask,cv2.MORPH_OPEN, kernel)

    # 膨胀把车变大一些
    dilate = cv2.dilate(open,kernel,iterations=3)

    # 闭操作
    close = cv2.morphologyEx(dilate,cv2.MORPH_CLOSE, kernel)

    # 查找轮廓
    contours, hierarchy = cv2.findContours(close,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    i=0
    while i<len(contours):
        x,y,w,h = cv2.boundingRect(contours[i]);
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255,255,0), 2)
        i = i+1

    cv2.imshow('video',frame)
    # cv2.imshow('video1',close)

    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

