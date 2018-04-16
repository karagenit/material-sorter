import serial
import time

bins = []

def init():
    return

# Wait for a serial signal from the arduino which
# says it's time to read an image.
def await_signal():
    return

def send(info):
    print("Sending serial data...")
    print("Length:", info.length)
    print("Width:", info.diameter)

    binIndex = find_or_insert(info)

    return

# Finds an existing bin for this bolt, or allocates a new one. Returns the bin index.
def find_or_insert(bolt):
    if bolt not in bins:
        bins.append(bolt)
    return bins.index(bolt)

def close():
    return
