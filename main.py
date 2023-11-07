import sys
sys.path.append("src")
sys.path.append("/home/redpi/code/rail_rider/src")
sys.path.append("/home/redpi/.local/lib/pyhton3.11/site-packages")



import time
# import RPi.GPIO as GPIO
# from rc import *
from motor_control import *
from linear_control import *
from contactor_control import *
from elight_control import *
import keyboard




Drive_Armed = False
Brush_Armed = False

# drive_armed_chanel = 6
# brush_armed_chanel = 7
# drive_trotle_chanel = 1
# brush_trotle_chanel = 3
# elight_chanel = 8
# linear_chanel = 10

drive_throttle = 0
brush_throttle = 0
elight_on = False
linear_state = 0

def inc_drive_throttle():
    if drive_throttle < 100:
        globals().update(drive_throttle = drive_throttle+1)
    print("Drive Throttle" + drive_throttle)
    
def dec_drive_throttle():
    if drive_throttle > 0:
        globals().update(drive_throttle = drive_throttle-1)
    print("Drive Throttle" + drive_throttle)
    
def kill_drive_throttle():
    globals().update(drive_throttle = 0)
    globals().update(Drive_Armed = False)
    print("Drive Throttle" + drive_throttle)
    print("Drive Disarmed")
    
def inc_brush_throttle():
    if brush_throttle < 100:
        globals().update(brush_throttle = brush_throttle+1)
    print("Brush Throttle" + brush_throttle)
    
def dec_brush_throttle():
    if brush_throttle > 100:
        globals().update(brush_throttle = brush_throttle-1)
    print("Brush Throttle" + brush_throttle)
    
def kill_brush_throttle():
    globals().update(brush_throttle = 0)
    globals().update(Brush_Armed = False)
    print("Brush Throttle" + brush_throttle)
    print("Brush Disarmed")
    
def arm_brush():
    globals().update(Brush_Armed = True)
    print("Brush Armed")
    
def arm_drive():
    globals().update(Drive_Armed = True)
    print("Drive Armed")
    
def turn_elight_on():
    globals().update(elight_on = True)
    print("Emergency Light On")
    
def turn_elight_off():
    globals().update(elight_on = True)
    print("Emergency Light Off")
    
def set_linear_up():
    globals().update(linear_state = 1)
    print("Linear State: Raising")
    
def set_linear_down():
    globals().update(linear_state = -1)
    print("Linear State: Lowering")
    
def set_linear_stop():
    globals().update(linear_state = 0)
    print("Linear State: Stopping")
    
# def update_armed():
#     if sig > 1500:
#         Drive_Armed = True
#     else:
#         Drive_Armed = False
#     if sig2 > 1500:
#         Brush_Armed = True
#     else:
#         Brush_Armed = False
        
def update_drive(drive_throttle):
    power = drive_throttle/100 #max is full
    if power > 1:
        power = 1
    if power < 0.02:
        power = 0
    set_drive_speed(power)

def update_brush(brush_throttle):
    power = brush_throttle/100 #max is half power
    if power > 0.5:
        power = 0.5
    if power < 0.02:
        power = 0
    set_drive_speed(power)
    
def update_elight(elight_on):
    if elight_on:
        activate_emergency_light()
    else:
        deactivate_emergency_light()
        
def update_linear(linear_state):
    if linear_state == -1:
        lower_linear()
    elif linear_state == 0:
        stop_linear()
    elif linear_state == 1:
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
    # while True:
    #     update_armed()
    #     if Drive_Armed:
    #         activate_drive_power()
    #         update_drive()
    #     else:
    #         deactivate_drive_power()
    #         set_drive_speed(0)
    #     if Brush_Armed:
    #         activate_brush_power()
    #         update_brush()
    #     else:
    #         deactivate_brush_power()
    #         set_brush_speed(0)
        
    #     update_elight()
    #     update_linear()
    #     display_sbus()
    #     time.sleep(1)
    keyboard.add_hotkey('w', inc_drive_throttle)
    keyboard.add_hotkey('q', dec_drive_throttle)
    keyboard.add_hotkey('x', kill_drive_throttle)
    keyboard.add_hotkey('s', inc_brush_throttle)
    keyboard.add_hotkey('a', dec_brush_throttle)
    keyboard.add_hotkey('z', kill_brush_throttle)
    keyboard.add_hotkey('shift + z', arm_brush)
    keyboard.add_hotkey('shift + x', arm_drive)
    keyboard.add_hotkey('l', turn_elight_on)
    keyboard.add_hotkey('k', turn_elight_off)
    keyboard.add_hotkey('i', set_linear_down)
    keyboard.add_hotkey('o', set_linear_stop)
    keyboard.add_hotkey('p', set_linear_up)
    
    while True:
        if Drive_Armed:
            activate_drive_power()
            update_drive(drive_throttle)
        else:
            deactivate_drive_power()
            set_drive_speed(0)
            globals().update(drive_throttle = 0)
        if Brush_Armed:
            activate_brush_power()
            update_brush(brush_throttle)
        else:
            deactivate_brush_power()
            set_brush_speed(0)
            globals().update(brush_throttle = 0)
            
        update_elight(elight_on)
        update_linear(linear_state)
        
initialize_robot()
main_control_loop()
