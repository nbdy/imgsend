from runnable import Runnable
from time import sleep
from requests import post

from . import CameraReader


class ImageSender(Runnable):
    url = None
    res = None
    every = None
    camera = None

    def __init__(self, url, every=30, res=(1920, 1080)):  # every 30 seconds
        Runnable.__init__(self)
        self.url = url
        self.every = every
        self.res = res
        self.camera = CameraReader(res)

    def send(self, img):
        post(self.url, files={"image": img}, data={"resolution": self.res})

    def work(self):
        self.send(self.camera.read())
        sleep(self.every)
