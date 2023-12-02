import cv2

# Initialize the USB camera (assuming it's connected and recognized)
camera = cv2.VideoCapture(0)  # Use 0 for the default camera

if not camera.isOpened():
    print("Cannot open camera")
    exit()

# Capture a frame
ret, frame = camera.read()

if not ret:
    print("Failed to capture frame")
    exit()

# Save the captured frame as an image
cv2.imwrite("test.jpg", frame)

# Release the camera
camera.release()
