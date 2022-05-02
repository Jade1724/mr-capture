import cv2
import numpy as np

video = cv2.VideoCapture(0)
image = cv2.imread('assets/ocean.jpg')
image = cv2.resize(image, (640, 480))


while True:
    ret, frame = video.read()

    # Convert BGR image to HSV image
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the background as a blue color in the following range
    lower_blue = np.array([32, 94, 70])
    upper_blue   = np.array([179, 255, 255])
    
    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    bg_mask = frame - res
    blue_screen = np.where(bg_mask==0, image, bg_mask)

    cv2.imshow('Frame', blue_screen)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()