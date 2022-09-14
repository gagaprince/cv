import sys
import cv2
import numpy as np

kernelopen = np.ones((7,7), np.uint8)
kernelclose = np.ones((9,9), np.uint8)

dotj = cv2.imread(sys.path[0]+'/dotj.png')
dotinj = cv2.imread(sys.path[0]+'/dotinj.png')

#开运算
open = cv2.morphologyEx(dotj,cv2.MORPH_OPEN, kernelopen)
#闭运算
close = cv2.morphologyEx(dotinj,cv2.MORPH_CLOSE, kernelclose)


cv2.imshow('dotj',dotj)
cv2.imshow('open',open)

cv2.imshow('dotinj',dotinj)
cv2.imshow('close',close)

cv2.waitKey(0)
cv2.destroyAllWindows()