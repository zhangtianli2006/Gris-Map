import numpy as np
import math
import cv2

img1 = cv2.imread("1.png", 0)
img2 = cv2.imread("2.png", 0)

detector = cv2.ORB_create()

flann_params = dict(
    algorithm=6, table_number=6, key_size=12, multi_probe_level=1  # 12  # 20
)  # 2

matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

kp1, desc1 = detector.detectAndCompute(img1, None)
kp2, desc2 = detector.detectAndCompute(img2, None)

raw_matches = matcher.knnMatch(desc1, desc2, 2)  # 2

good = []

for m, n in raw_matches:
    if m.distance < 0.7 * n.distance:
        good.append(m)

if len(good) > 10:
    src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)

    matchesMask = mask.ravel().tolist()

else:
    print("Not enough matches are found - %d/%d" % (len(good), 10))
    matchesMask = None
draw_params = dict(
    matchColor=(0, 255, 0),  # draw matches in green color
    singlePointColor=(0, 0, 255),
    matchesMask=matchesMask,
    flags=2,
)  # draw only inliers

vis = cv2.drawMatches(img1, kp1, img2, kp2, good, None, **draw_params)

cv2.imwrite("resault.jpg", vis)

# https://www.jianshu.com/p/a63265962273
