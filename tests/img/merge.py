import cv2
import os

cv2.ocl.setUseOpenCL(False)

img_dir = "img_merge_test"
# img_dir = "frame_test"
output = "result.jpg"
conf_path = "{}/files.conf".format(img_dir)

fp = open(conf_path, "r")
filenames = [each.rstrip("\r\n") for each in fp.readlines()]
print(filenames)

images = []
for img_name in filenames:
    img = cv2.imread(os.path.join(img_dir, img_name))
    images.append(img)

stitcher = cv2.Stitcher_create()
status, res = stitcher.stitch(images)

cv2.imwrite(os.path.join(img_dir, output), res)

# https://blog.csdn.net/yy2yy99/article/details/103034651