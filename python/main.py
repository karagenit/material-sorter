#!/usr/bin/env python3

import arduino
import vision

run = True
while run:
    arduino.await_signal()
    # grab image
    vision.read_image()
    # process image
    # print results
    print("Image Processed")
    run = False
