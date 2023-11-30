import cv2
import pyrealsense2
from realsense_depth import *
import time
import numpy as np

point = (320, 240)
scary_range = 1500
# def show_distance(event, x, y, args, params):
#     global point
#     point = (x, y)

# Initialize Camera Intel Realsense

dc1 = DepthCamera()
dc2 = DepthCamera()
pyrealsense2.hole_filling_filter(2)


while True:
    ret, depth_frame, color_frame = dc1.get_frame()

    # Show distance for a specific point
    # cv2.circle(color_frame, point, 4, (0, 0, 255))
    distance = depth_frame[point[1], point[0]]
    # if distance > 0:
    print(distance)
    if distance < scary_range and distance > 0:
        print("$$$$$$$$ KILLLLLL $$$$$$$$$$$$$$$")
    time.sleep(0.02)

    # cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

    # cv2.imshow("depth frame", depth_frame)
    # cv2.imshow("Color frame", color_frame)
    # key = cv2.waitKey(1)
    # if key == 27:
    #     break