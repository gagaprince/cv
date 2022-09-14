import sys
import cv2

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(sys.path[0]+'/cat.jpg')

img1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, img2 = cv2.threshold(img1, 100, 255,cv2.THRESH_BINARY)

# 查找轮廓
contours, hierarchy = cv2.findContours(img2,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(contours)
# 绘制轮廓
cv2.drawContours(img, contours, -1, (255,255,0), 1)

cv2.imshow('img',img)
cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()