import sys
import cv2

#cv2.namedWindow('img', cv2.WINDOW_NORMAL)
img = cv2.imread(sys.path[0]+'/cat.jpg')
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()