import cv2
import time
import numpy as np

camera = cv2.VideoCapture(0)  # Use 0 for the default camera

if not camera.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Calculate the average pixel value
    average_pixel_value = np.mean(frame)
    print(f"Average pixel value: {average_pixel_value}")

    # Assign the captured frame to the variable L_front
    L_front = frame

    # Save the captured frame as 'test.jpg' (optional)
    cv2.imwrite("test.jpg", frame)

    # Display the captured frame (optional)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Wait for 1 second before capturing the next frame
    time.sleep(1)

# Release the camera and close the OpenCV windows
camera.release()
cv2.destroyAllWindows()
