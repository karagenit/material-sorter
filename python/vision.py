import numpy as np
import cv2 as cv

# Reads an image from either a test file or the picamera
def read_image():
    return cv.imread('opencv.jpg')

def filter_image(original):
    #img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    lower = np.array([100, 0, 0])
    upper = np.array([255, 100, 100])
    return cv.inRange(original, lower, upper)


def process_image():
    return
