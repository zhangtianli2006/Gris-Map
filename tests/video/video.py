import time
import cv2
import os

cap = cv2.VideoCapture("example.mp4")
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

k = 0

while True:
    ret, frame = cap.read()
    src = cv2.resize(frame, (frame_width, frame_height), interpolation=cv2.INTER_CUBIC)
    cv2.imwrite(os.path.join("frame", "{}.png".format(k)), src)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

    k += 1
    time.sleep(1 / fps)

# https://blog.csdn.net/j18423532754/article/details/106518434/