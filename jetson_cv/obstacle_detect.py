import numpy
import cv2
from .pyrealsense2 import *

fx = 942.8          # lense focal length
baseline = 54.8     # distance in mm between the two cameras
disparities = 128   # num of disparities to consider
block = 31          # block size to match
units = 0.001       # depth units

sbm = cv2.StereoBM_create(numDisparities=disparities,
                          blockSize=block)

disparity = sbm.compute(left, right)

depth = np.zeros(shape=left.shape).astype(float)
depth[disparity > 0] = (fx * baseline) / (units * disparity[disparity > 0])