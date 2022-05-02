import cv2
from cv2 import VideoCapture
import numpy as np

video = VideoCapture(0)

while True:
    ret, frame = video.read()

    # Convert BGR image to HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the background as a blue color in the following range
    lower_blue = np.array([32, 94, 70])
    upper_blue   = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    cv2.imshow('Frame', mask)
    if cv2.waitKey(1) == ord('q'):
        break


    # dark blue
    # h 242
    # s 94
    # v 60

    # lighter blue 
    # h 242
    # s 83
    # v 100

video.release()
cv2.destroyAllWindows()