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
LENGTHS = np.arange(1, 4, 0.25)

# Just #10 and 1/4"
DIAMETERS = np.array([ 0.19, 0.25 ])

class Bolt:
    def __init__(self, length, diameter, threads):
        self.length = length
        self.diameter = diameter
        self.threads = threads

    def __eq__(self, other):
        return self.length == other.length and self.diameter == other.diameter and self.threads == other.threads

def filter_image(original):
    #img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    lower = np.array([0, 0, 0])
    upper = np.array([240, 240, 240])
    bw = cv.inRange(original, lower, upper)

    # Removes random one-pixel noise
    kernel = np.ones((3,3), np.uint8)
    eroded = cv.erode(bw, kernel, iterations = 1)

    # Fills in gaps in main image
    kernel = np.ones((8,8), np.uint8)
    dilated = cv.dilate(eroded, kernel, iterations = 1)

    # Gets us back to original size ish for length calculations
    kernel = np.ones((5,5), np.uint8)
    final = cv.erode(dilated, kernel, iterations = 1)

    return final

def process_image(original, filtered):
    edges = cv.Canny(filtered, 100, 200)
    (_, contours, _) = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # TODO: choose 'ideal' contour
    primaryContour = contours[0]
    # Gives us a tuple: ((center x,y), (width, height), rotationAngle)
    boundingRect = cv.minAreaRect(primaryContour)

    # Length is the longer of the two
    length = pixel_to_inch(max(boundingRect[1][0], boundingRect[1][1]), LENGTHS)
    width  = pixel_to_inch(min(boundingRect[1][0], boundingRect[1][1]), DIAMETERS)

    # DEBUG
    drawnImg = original.copy()
    cv.drawContours(drawnImg, contours, -1, (0,255,0), 2)
    box = cv.boxPoints(boundingRect)
    box = np.int0(box)
    cv.drawContours(drawnImg,[box],0,(0,0,255),2)
    cv.imshow("Edges", drawnImg)

    # We hardcode 1 thread per inch until we can vision process that
    return Bolt(length, width, 1)

# Converts a pixel len/width to inches and finds the nearest in the array
def pixel_to_inch(value, array):
    inches = value / PPI
    idx = (np.abs(array-inches)).argmin()
    return array[idx]
