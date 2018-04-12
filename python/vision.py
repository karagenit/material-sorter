import numpy as np
import cv2 as cv

def read_image():
    img = cv.imread('opencv.jpg')
    #img = cv.cvtColor(img, cv.COLOR_RGB2HSV)
    lower = np.array([100, 0, 0])
    upper = np.array([255, 100, 100])
    mask = cv.inRange(img, lower, upper)
    cv.imshow('Original', img)
    cv.imshow('BGR Filter', mask)
    cv.waitKey(0)
    cv.destroyAllWindows()
