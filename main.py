import time
import RPi.GPIO as GPIO
from /src/rc import *
from /src/motor_control import *
from /src/linear_control import *
from /src/contactor_control import *
from /src/elight_control import *


while True:
    test_func()
    set_drive_speed(0.2)
    set_brush_speed(0.2)
    

