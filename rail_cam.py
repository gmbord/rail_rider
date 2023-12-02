import picamera
from time import sleep

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 720)  # Set the resolution
    camera.start_preview()
    sleep(5)  # Allow time for the camera to adjust to light
    camera.capture("image.jpg")  # Capture an image and save it as image.jpg
    camera.stop_preview()
