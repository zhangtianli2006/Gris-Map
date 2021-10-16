import numpy as np
import cv2

delta_x = -946
delta_y = 637

img1 = cv2.imread("1.png")
img2 = cv2.imread("2.png")

img3 = cv2.copyMakeBorder(img1, 0, 2000, 0, 2000, cv2.BORDER_CONSTANT)
# cv2.imwrite("border.png", img3);

tot_rows = img2.shape[0] + img1.shape[0] - delta_x
tot_cols = img2.shape[1] + img1.shape[1] - delta_y

# res = np.matrix()

for i in range(0, img2.shape[0]):
    for j in range(0, img2.shape[1]):
        img3[i][1000 + j] = img2[i][j]

for i in range(0, img1.shape[0]):
    for j in range(0, img1.shape[1]):
        img3[int(delta_y + i)][1000 + int(delta_x + j)] = img1[i][j]

cv2.imwrite("resault.png", img3);

# print(len(img2.tolist()))
