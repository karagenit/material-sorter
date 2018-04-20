from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv

camera = None
rawCapture = None

def init():
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    time.sleep(0.1)
    return

def read():
    camera.capture(rawCapture, format="bgr")
    return rawCapture.array
