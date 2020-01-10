import cv2
import time

from detect import Detect
from display import Display
from imutils.video import FileVideoStream
from imutils.video import FPS
import imutils

class TestDetection():
    def __init__(self, type, src, w=None, h=None):
        self.type = type
        if type == 'vid':
            self.w = w
            self.h = h

        self.src = src

        range = ([0,100,100], [40,255,255])
        self.Detect = Detect(range)

    def detect(self, show=False):
        if self.type == 'img':
            self.detect_img(show)
            pass
        if self.type == 'vid':
            self.detect_vid(show)

    def detect_img(self, show):
        frame = self.Detect.detect_frame(self.src)
        if show:
            cv2.imshow('frame', frame)
            cv2.waitKey(0)
        return frame

    def detect_vid(self, show):
        disp = Display(self.w*2, self.h)
        print('Starting...')

        i = 0
        fps = FPS().start()
        while self.src.more():
            frame = self.src.read()
            if frame is None: 
                break
            d_frame = self.Detect.detect_frame(frame)
            disp.paint(d_frame)
            fps.update()
            time.sleep(0.01)
            fps.stop()
            print('fps: %f at frame %i' % (fps.fps(),i))
            i += 1
        cv2.destroyAllWindows()
        self.src.stop()


#img first
img = cv2.imread('test_img/game.jpg')
vid = FileVideoStream('test_vid/field.mp4').start()
test = TestDetection('vid', vid, 640, 360)
test.detect(True)
