#!/usr/bin/env python3

import sys
import cv2 as cv

import camera
#import test_camera as camera
import arduino
#import test_arduino as arduino
import vision

arduino.init()
camera.init()

print("Libraries Loaded.")

try:
    while True:
        arduino.await_signal()

        img = camera.read()
    #   cv.imshow('Original', img)

        filtered = vision.filter_image(img)
    #   cv.imshow('Filtered', filtered)

        info = vision.process_image(img, filtered)

        print("Image Processed")
        arduino.send(info)

    #   cv.waitKey(0)
    #   cv.destroyAllWindows()
except (KeyboardInterrupt, SystemExit):
    print("Exiting...")
finally:
    arduino.close()
