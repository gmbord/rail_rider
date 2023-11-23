import cv2
import pyrealsense2
from realsense_depth import *


dc = DepthCamera()
ret, depth_frame, color_frame = dc.get_frame()
cv2.imhow("Color frame", color_frame)
cv2.waitKey()