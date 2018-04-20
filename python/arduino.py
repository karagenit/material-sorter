import serial
import time

serialPort = 0

# List of what each bin contains. As we find new bolts, we allocate new bins for them.
#   Obviously, the physical device has finite bins, but the arduino handles having the
#   "overflow" bin. Though, because we send bytes, we have an effective limit of 256.
bins = []

def init():
    global serialPort
    serialPort = serial.Serial("/dev/ttyACM0", 9600)
    time.sleep(0.25)
    # TODO: handshake byte?
    return

# Wait for a serial signal from the arduino which
# says it's time to read an image.
def await_signal():
    return

def send(info):
    global serialPort
    print("Sending serial data...")
    print("Length:", info.length)
    print("Width:", info.diameter)

    binIndex = find_or_insert(info)

    print("Bin:", binIndex)

    serialPort.write(bytes([binIndex]))
    return

# Finds an existing bin for this bolt, or allocates a new one. Returns the bin index.
def find_or_insert(bolt):
    global bins
    if bolt not in bins:
        bins.append(bolt)
    return bins.index(bolt)

def close():
    global serialPort
    serialPort.close()
    return
