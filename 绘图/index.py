import cv2
import os

# print(os.getcwd())

cap = cv2.VideoCapture(os.getcwd()+"/video.mp4")

while True:
    rel, frame = cap.read()

    # 画线
    # cv2.line(frame, (100,100), (600,400), (255,255,0), 5)
    
    # 画矩形
    # cv2.rectangle(frame, (100,100), (600,400), (255,255,0))

    # 画圆
    # cv2.circle(frame, (300,300), 100, (255,255,0))

    # 文字
    cv2.putText(frame, "COOL", (300,300), 1, 5, (255,255,0), 10)

    cv2.imshow('video',frame)


    key = cv2.waitKey(1)
    if(key == 27):
        break
cv2.destroyAllWindows()

