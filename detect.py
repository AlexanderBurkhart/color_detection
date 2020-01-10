import cv2
import numpy as np

class Detect():
    def __init__(self, range):
        self.d_range = range

    def detect_frame(self, src):
        #color detection
        lower = np.array(self.d_range[0], dtype='uint8')
        upper = np.array(self.d_range[1], dtype='uint8')
        mask = cv2.inRange(src, lower, upper)
        output = cv2.bitwise_and(src, src, mask=mask)
        return np.hstack([src, output])
