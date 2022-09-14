import sys
import cv2
import numpy as np

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(sys.path[0]+'/cat.jpg')

kernel = np.ones((5,5), np.float32) / 25

new_img = cv2.filter2D(img, -1, kernel)

cv2.imshow('img',img)
cv2.imshow('new_img',new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()