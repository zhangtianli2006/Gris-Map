import cv2
import os

cv2.ocl.setUseOpenCL(False)

img_dir = "img_merge_test"
output = "result.jpg"
conf_path = "{}/files.conf".format(img_dir)

fp = open(conf_path, "r")
filenames = [each.rstrip("\r\n") for each in fp.readlines()]

first = cv2.imread(os.path.join(img_dir, filenames[0]))
cv2.imwrite(os.path.join(img_dir, output), first)
filenames.remove(filenames[0])

for img_name in filenames:
    images = []
    base = cv2.imread(os.path.join(img_dir, output))
    img = cv2.imread(os.path.join(img_dir, img_name))
    images.append(base)
    images.append(img)

    try:
        stitcher = cv2.Stitcher_create()
        status, res = stitcher.stitch(images)
        cv2.imwrite(os.path.join(img_dir, output), res)
    except BaseException:
        print("[Err] on img {}".format(img_name))
    else:
        print("img {}".format(img_name))

