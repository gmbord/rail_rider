import sys
sys.path.append("src")

import time
import RPi.GPIO as GPIO
from rc import *
from motor_control import *
from linear_control import *
from contactor_control import *
from elight_control import *




Drive_Armed = False
Brush_Armed = False

drive_armed_chanel = 6
brush_armed_chanel = 7
drive_trotle_chanel = 1
brush_trotle_chanel = 3
elight_chanel = 8
linear_chanel = 10




def update_armed():
    sig = read_sbus_chanel(drive_armed_chanel)
    sig2 = read_sbus_chanel(brush_armed_chanel)
    if sig >= 1000 and sig <= 2000:
        if sig > 1500:
            Drive_Armed = True
        else:
            Drive_Armed = False
    else:
        Drive_Armed = False
    if sig2 >= 1000 and sig2 <= 2000:
        if sig2 > 1500:
            Brush_Armed = True
        else:
            Brush_Armed = False
    else:
        Brush_Armed = False
        
def update_drive():
    sig = read_sbus_chanel(drive_trotle_chanel)
    if sig >= 1000 and sig <= 2000:
        power = (sig - 1000) / 1000 #max is full
        if power > 1:
            power = 1
        if power < 0.02:
            power = 0
        set_drive_speed(power)

def update_brush():
    sig = read_sbus_chanel(brush_trotle_chanel)
    if sig >= 1000 and sig <= 2000:
        power = (sig - 1000) / 2000 #max is half power
        if power > 0.5:
            power = 0.5
        if power < 0.02:
            power = 0
        set_drive_speed(power)
    
def update_elight():
    sig = read_sbus_chanel(elight_chanel)
    if sig >= 1000 and sig <= 2000:
        if sig > 1500:
            activate_emergency_light()
        else:
            deactivate_emergency_light()
        
def update_linear():
    sig = read_sbus_chanel(linear_chanel)
    if sig < 1200 and sig >= 1000:
        lower_linear()
    elif sig > 1200 and sig <= 1800:
        stop_linear()
    elif sig > 1800 and sig <= 2000:
        raise_linear()
    else:
        stop_linear()
    
def initialize_robot():
    deactivate_brush_power()
    deactivate_drive_power()
    activate_emergency_light()
    stop_linear()
    set_drive_speed(0)
    set_brush_speed(0)

def main_control_loop():
    while True:
        update_armed()
        if Drive_Armed:
            activate_drive_power()
            update_drive()
        else:
            deactivate_drive_power()
            set_drive_speed(0)
        if Brush_Armed:
            activate_brush_power()
            update_brush()
        else:
            deactivate_brush_power()
            set_brush_speed(0)
        
        update_elight()
        update_linear()
        display_sbus()
        time.sleep(1)

initialize_robot()
main_control_loop()
