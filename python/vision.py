import numpy as np
import cv2 as cv

def read_image():
    img = cv.imread('opencv.jpg', 0)
    cv.imshow('image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()
