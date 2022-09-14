import sys
import cv2
import numpy as np

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(sys.path[0]+'/j.png')

kernel = np.ones((3,3), np.uint8)
#腐蚀
img1 = cv2.erode(img, kernel, iterations=2)
#膨胀
# img1 = cv2.dilate(img, kernel, iterations=2)


cv2.imshow('img',img)
cv2.imshow('img1',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()