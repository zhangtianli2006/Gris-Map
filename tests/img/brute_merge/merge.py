import numpy as np
import cv2

img1 = cv2.imread("1.png")
# img2 = cv2.imread("2.png")

rows, cols = img1.shape[0:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img1, M, (cols, rows))

# cv2.imwrite("move.png", dst)

cv2.imwrite("move.png", dst)
# img2[img2.shape[0]:img2.shape[0] + img1.shape[0], img2.shape[1]:img2.shape[1] + img1.shape[1]] = img1
