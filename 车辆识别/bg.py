import cv2
import os

# print(os.getcwd())

cap = cv2.VideoCapture(os.getcwd()+"/车辆识别/video.mp4")

bgsubmog = cv2.bgsegm.createBackgroundSubtractorMOG()

while True:
    rel, frame = cap.read()

    # 灰度
    # cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # # 去噪
    # blur = cv2.GaussianBlur(frame, (3,3),5)

    mask = bgsubmog.apply(frame)

    
    cv2.imshow('video',frame)
    cv2.imshow('video1',mask)


    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

