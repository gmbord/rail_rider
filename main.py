import time
import RPi.GPIO as GPIO
from rc import *
from motor_control import *
from linear_control import *
from contactor_control import *
from elight_control import *


while True:
    test_func()
    set_drive_speed(0.2)
    set_brush_speed(0.2)
    

