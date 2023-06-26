import cv2, numpy as np
import mss

with mss.mss() as sct:
    mon = {"left" : -1920, "top": 0, "height" : 1920, "width" : 1080}

    low_blue = np.array([0, 0, 50])
    high_blue  = np.array([100, 255, 255])


    while True:
        img = np.array(sct.grab(mon))
        rgb_mon = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        mask = cv2.inRange(rgb_mon, low_blue, high_blue)

        cv2.imshow('Test', mask)
        if cv2.waitKey(33) == ord('q'):
            break