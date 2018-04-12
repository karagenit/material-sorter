import numpy as np
import cv2 as cv

class Bolt:
    def __init__(self, length, diameter, threads):
        self.length = length
        self.diameter = diameter
        self.threads = threads

# Reads an image from either a test file or the picamera
def read_image():
    return cv.imread('opencv.jpg')

def filter_image(original):
    #img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    lower = np.array([100, 0, 0])
    upper = np.array([255, 100, 100])
    bw = cv.inRange(original, lower, upper)

    kernel = np.ones((3,3), np.uint8)
    eroded = cv.erode(bw, kernel, iterations = 1)

    return eroded


def process_image(original, filtered):
    edges = cv.Canny(filtered, 100, 200)
    (_, contours, _) = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    print("Contour count:", len(contours))

    drawnImg = original.copy()
    cv.drawContours(drawnImg, contours, -1, (0,255,0), 3)
    cv.imshow("Edges", drawnImg)

    return Bolt(2, 0.25, 20)
