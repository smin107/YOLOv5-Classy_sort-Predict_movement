import cv2
import numpy as np
import sys

src = cv2.imread(r'.\inference\images\cctv_school_zone_000200_00001.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (80, 80, 80), (150, 150, 150))
dst2 = cv2.inRange(src_hsv, (0, 0, 0), (240, 80, 80))

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()