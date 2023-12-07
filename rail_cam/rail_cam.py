import cv2
import time
from clean_quantification import clean_quantification

# cameras ordered left-front (LF), LB, RF, RB
num_cameras = 4
cameras = [cv2.VideoCapture(i) for i in range(num_cameras)]

for idx, camera in enumerate(cameras):
    if not camera.isOpened():
        print(f"Cannot open camera {idx}")
        exit()

while True:
    frames = []

    for camera in cameras:
        ret, frame = camera.read()

        if not ret:
            print("Failed to capture frame")
            break

        frames.append(frame)

    # # Save the captured frame as 'test.jpg' (optional)
    # cv2.imwrite("test.jpg", frame)

    # # Display the captured frame (optional)
    # cv2.imshow("Frame", frame)

    clean_vals = [clean_quantification(frame) for frame in frames]

    print(clean_vals)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    # Wait for 1 second before capturing the next frame
    time.sleep(1)

# Release the cameras and close the OpenCV windows
for camera in cameras:
    camera.release()
cv2.destroyAllWindows()
