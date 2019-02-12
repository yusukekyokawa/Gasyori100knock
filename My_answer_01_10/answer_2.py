import cv2


img = cv2.imread("assets/imori.jpg")
r = img[:, :, 2].copy()
g = img[:, :, 1].copy()
b = img[:, :, 0].copy()

out =