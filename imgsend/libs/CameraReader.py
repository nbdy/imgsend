from time import sleep
from picamera.array import PiRGBArray
from picamera import PiCamera


class CameraReader(object):
    camera = None
    raw = None

    def __init__(self, res=(1920, 1080)):
        self.camera = PiCamera()
        self.camera.resolution = res
        self.raw = PiRGBArray(self.camera, size=res)
        sleep(0.1)  # let the camera warm up or something

    def read(self):
        self.camera.capture(self.raw, format="bgr")
        return self.raw.array
