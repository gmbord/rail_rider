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
ctx = rs.context()
devices = ctx.query_devices()
print(devices[0])
print(devices[1])

# Configure depth and color streams...
# ...from Camera 1
pipeline_1 = rs.pipeline()
config_1 = rs.config()
config_1.enable_device('242322075040')
config_1.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config_1.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
# ...from Camera 2
pipeline_2 = rs.pipeline()
config_2 = rs.config()
config_2.enable_device('238222072344')
config_2.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config_2.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# dc1 = DepthCamera()
# dc2 = DepthCamera()
# pyrealsense2.hole_filling_filter(2)


# while True:
#     ret, depth_frame, color_frame = dc1.get_frame()
#     ret2, depth_frame2, color_frame2 = dc2.get_frame()
#     # Show distance for a specific point
#     # cv2.circle(color_frame, point, 4, (0, 0, 255))
#     distance = depth_frame[point[1], point[0]]
#     distance2 = depth_frame2[point[1], point[0]]
#     # if distance > 0:
#     print("DISTANCE 1 ", distance)
#     print("DISTANCE 2 ", distance2)
#     if distance < scary_range and distance > 0:
#         print("$$$$$$$$ KILLLLLL  1   $$$$$$$$$$$$$$$")
#     if distance2 < scary_range and distance > 0:
#         print("$$$$$$$$ KILLLLLL  2   $$$$$$$$$$$$$$$")
#     time.sleep(0.02)

#     # cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

#     # cv2.imshow("depth frame", depth_frame)
#     # cv2.imshow("Color frame", color_frame)
#     # key = cv2.waitKey(1)
#     # if key == 27:
#     #     break