#!/usr/bin/env python3

import arduino
import vision
import cv2 as cv

run = True
while run:
    arduino.await_signal()

    img = vision.read_image()
    cv.imshow('Original', img)

    filtered = vision.filter_image(img)
    cv.imshow('Filtered', filtered)

    info = vision.process_image(img, filtered)

    print("Image Processed")
    arduino.send(info)

    cv.waitKey(0)
    cv.destroyAllWindows()
    run = False
