import cv2
import time
import numpy as np
from clean_quantification import clean_quantification

camera = cv2.VideoCapture(0)  # Use 0 for the default camera

if not camera.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Assign the captured frame to the variable L_front
    L_front = frame

    # # Save the captured frame as 'test.jpg' (optional)
    # cv2.imwrite("test.jpg", frame)

    # # Display the captured frame (optional)
    # cv2.imshow("Frame", frame)

    clean_val = clean_quantification(frame)

    print(clean_val)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Wait for 1 second before capturing the next frame
    time.sleep(1)

# Release the camera and close the OpenCV windows
camera.release()
cv2.destroyAllWindows()
