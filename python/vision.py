import numpy as np
import cv2 as cv

# This is used for calculating bolt info based on the processed image.

# Pixels Per Inch - this is currently theoretical based on a 1920x1080p camera
#   held 6 inches away from the table with a 90 degree horizontal FOV. (90 degree FOV @6" gives
#   12" across camera horizontally, so 1920/12). Not sure how this will handle bolts not facing
#   horizontally.
PPI = 160

# This determines how precisely we should try to sort/categorize bolts (e.g. by 1/4" lengths)
#   Higher precision results in less accuracy (higher rate of false sorting).
LENGTHS = [ 1, 1.25, 1.5, 1.75, 2 ]

# Just #10 and 1/4"
DIAMETERS = [ 0.19, 0.25 ]

class Bolt:
    def __init__(self, length, diameter, threads):
        self.length = length
        self.diameter = diameter
        self.threads = threads

# Reads an image from either a test file or the picamera
def read_image():
    return cv.imread('bolt.jpg')

def filter_image(original):
    #img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([240, 240, 240])
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
