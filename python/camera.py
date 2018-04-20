from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2 as cv

camera = None
rawCapture = None

def init():
    global camera
    global rawCapture
    camera = PiCamera()
    rawCapture = PiRGBArray(camera)
    time.sleep(0.1)
    return

def read():
    global camera
    global rawCapture
    camera.capture(rawCapture, format="bgr")
    return rawCapture.array
