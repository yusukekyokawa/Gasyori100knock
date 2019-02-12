import numpy as np
import cv2

img = cv2.imread("imori.jpg")

out = img.copy()

out = out // 64 * 64 + 32

cv2.imwrite("out_6.jpg", out)