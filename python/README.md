# Python

## Using Debug

Eventually, we'll have a `camera.py` and `test_camera.py` (and a test pair for arduino) which differ by either loading a dummy image file for testing or actually reading the pi camera (which we can't do on my laptop). 

At the start of the main file, we'll read the `-t` flag (from `sys.argv[1]`) and either `import camera` or `import test_camera as camera`. 
