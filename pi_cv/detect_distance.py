import cv2
import pyrealsense2
from realsense_depth import *
import time
import numpy as np
import pigpio
from ultralytics import YOLO

FRONT_CAM = 17
BACK_CAM = 27

pi = pigpio.pi()

pi.set_mode(FRONT_CAM , pigpio.OUTPUT)
pi.set_mode(BACK_CAM , pigpio.OUTPUT)

pi.write(FRONT_CAM , 0)
pi.write(BACK_CAM , 0)

point = (320, 240)
scary_range = 1500
consecutive_front = 0
consecutive_back = 0
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
# config_1.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline_1.start(config_1)
# ...from Camera 2
pipeline_2 = rs.pipeline()
config_2 = rs.config()
config_2.enable_device('238222072344')
config_2.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
# config_2.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline_2.start(config_2)

def get_frame(pipeline):
    frames = pipeline.wait_for_frames()
    depth_frame = frames.get_depth_frame()
    # color_frame = frames.get_color_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    # color_image = np.asanyarray(color_frame.get_data())
    if not depth_frame:
        return False, None
    return True, depth_image

# dc1 = DepthCamera()
# dc2 = DepthCamera()
pyrealsense2.hole_filling_filter(2)

def get_distance_1():
    ret, depth_frame = get_frame(pipeline_1)
    distance = depth_frame[point[1], point[0]]
    print("DISTANCE 1 ", distance)
    return(distance)

def get_distance_2():
    ret, depth_frame = get_frame(pipeline_2)
    distance = depth_frame[point[1], point[0]]
    print("DISTANCE 2 ", distance)
    return(distance)

while True:
    distance_1 = get_distance_1()
    distance_2 = get_distance_2()
    if distance_1 < scary_range and distance_1 > 0:
        consecutive_front += 1
    else:
        consecutive_front = 0
        
    if distance_2 < scary_range and distance_2 > 0:
        consecutive_back += 1
    else:
        consecutive_back = 0
        
    if consecutive_front > 2:
        pi.write(FRONT_CAM , 1)
        print("$$$$$$$$ KILLLLLL  FRONT   $$$$$$$$$$$$$$$")
    else:
        pi.write(FRONT_CAM , 0)
        
    if consecutive_back > 2:
        pi.write(BACK_CAM , 1)
        print("$$$$$$$$ KILLLLLL  BACK   $$$$$$$$$$$$$$$")
    else:
        pi.write(BACK_CAM , 0)
        
    time.sleep(0.02)

#     # cv2.putText(color_frame, "{}mm".format(distance), (point[0], point[1] - 20), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 2)

#     # cv2.imshow("depth frame", depth_frame)
#     # cv2.imshow("Color frame", color_frame)
#     # key = cv2.waitKey(1)
#     # if key == 27:
#     #     break