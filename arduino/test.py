#!/usr/bin/env python3

import serial
import time
import sys

serialPort = serial.Serial("/dev/ttyACM0", 9600)

while True:
    serialPort.write(bytes([int(input("Enter Bin #: "))]))
