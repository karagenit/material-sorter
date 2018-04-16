#!/usr/bin/env python3

import sys
import cv2 as cv

testMode = len(sys.argv) > 1 and sys.argv[1] == "-t"

if(testMode):
    import test_camera as camera
else:
    import camera

#import arduino
import test_arduino as arduino
import vision

arduino.init()

run = True
while run:
    arduino.await_signal()

    img = camera.read()
    cv.imshow('Original', img)

    filtered = vision.filter_image(img)
    cv.imshow('Filtered', filtered)

    info = vision.process_image(img, filtered)

    print("Image Processed")
    arduino.send(info)

    cv.waitKey(0)
    cv.destroyAllWindows()
    run = False

arduino.close()
