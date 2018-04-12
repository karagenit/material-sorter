#!/usr/bin/env python3

import arduino
import vision
import cv2 as cv

run = True
while run:
    arduino.await_signal()

    img = vision.read_image()
    cv.imshow('Original', img)

    img = vision.filter_image(img)
    cv.imshow('Filtered', img)

    info = vision.process_image(img)

    print("Image Processed")
    print("Length:", info.length, "inches.")
    cv.waitKey(0)

    cv.destroyAllWindows()
    run = False
