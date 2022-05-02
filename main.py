import cv2
from cv2 import VideoCapture
import numpy as np

video = VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()