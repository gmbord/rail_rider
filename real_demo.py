import sys
sys.path.append("src")
sys.path.append("/home/redpi/code/rail_rider/src")
sys.path.append("/home/redpi/.local/lib/pyhton3.11/site-packages")



import time
from rc import *
from motor_control import *
from linear_control import *
from contactor_control import *
from peripheral_control import *
from headlight_control import *
from stereocam_control import *
from gobutton_control import *
import keyboard
import serial

def serial_reconnect():
    output = "jibberish"
    out = output.encode('utf-8')
    try:
        globals().update(ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1))
        ser.write(out)
        print("Serial Reconnected")
    except:
        time.sleep(0.3)
        print("Reconnecting....")
        serial_reconnect()
        
#REMEMBER TO UNCOMMENT

try:
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    time.sleep(1)
except:
    serial_reconnect()





Drive_Armed = False
Brush_Armed = False

State = 1

Frames_Dropped = 0

# RC CONTROLLER CHANELS
drive_armed_chanel = 6 # Switch 2, LOW: 192, High: 1792 
brush_armed_chanel = 7 # Switch 3, LOW: 192, High: 1792 
drive_trotle_chanel = 1 # Throttle Stick, LOW: 192, HIOH: 1792
brush_trotle_chanel = 8 # Switch 4, LOW: 192, MID: 992, HIGH: 1792
linear_chanel = 5 #Switch 1, LOW: 192, MID: 992, HIGH: 1792
rudder_chanel = 4 # Throttle stick x axis
elevator_chanel = 3 # elevator for horn

drive_throttle = 0
brush_throttle = 0
elight_on = True
linear_state = 0

REVERSE = False
demo_running = True  

    
def update_armed():
    if read_sbus_chanel(drive_armed_chanel) > 1500:
        if read_sbus_chanel(drive_trotle_chanel) < 200 and Drive_Armed == False:
            globals().update(Drive_Armed = True)
    else:
        globals().update(Drive_Armed = False)
    if read_sbus_chanel(brush_armed_chanel) > 1500:
        globals().update(Brush_Armed = True)
    else:
        globals().update(Brush_Armed = False)
        
def update_drive():
    # Throttle Stick, LOW: 192, HIOH: 1792
    sig = read_sbus_chanel(drive_trotle_chanel)
    high = 1792
    low = 192
    power = (sig - low) / (high - low)
    # power = drive_throttle/100 #max is full
    if power > 1:
        power = 1
    if power < 0.02:
        power = 0
    #REMEMBER TO UNCOMMENT
    write_serial_d(power)
    
def update_drive_zero():
    power = 0
    #REMEMBER TO UNCOMMENT
    write_serial_d(power)

def update_brush():
    # Switch 4, LOW: 192, MID: 992, HIGH: 1792
    # power = brush_throttle/100 #max is half power
    sig = read_sbus_chanel(brush_trotle_chanel)
    low = 192
    mid = 992
    high = 1792
    if sig > high - 100 and sig < high + 50:
        power = 0.6
    elif sig < mid + 100 and sig > mid - 100:
        power = 0.3
    else:
        power = 0
    #REMEMBER TO UNCOMMENT
    write_serial_b(power)
    
def update_brush_zero():
    power = 0
    #REMEMBER TO UNCOMMENT
    write_serial_b(power)
    
def update_elight(elight_on):
    if elight_on:
        activate_emergency_light()
    else:
        deactivate_emergency_light()
        
def update_linear():
    #Switch 1, LOW: 192, MID: 992, HIGH: 1792
    sig = read_sbus_chanel(linear_chanel)
    low = 192
    mid = 992
    high = 1792
    if sig > high - 100 and sig < high + 50:
        raise_linear()
    elif sig < mid + 100 and sig > mid - 100:
        stop_linear()
    elif sig < low + 50 and sig > low - 50:
        lower_linear()
    else:
        stop_linear()
        
def update_horn():
    sig = read_sbus_chanel(elevator_chanel)
    if sig < 300:
        activate_horn()
    else:
        deactivate_horn()
        
def update_brakes():
    sig = read_sbus_chanel(drive_trotle_chanel)
    
    if sig < 215:
        activate_brakes()
        reverse_sig = read_sbus_chanel(rudder_chanel)
        if reverse_sig < 300:
            activate_rear_brakelights()
        else:
            activate_front_brakelights()
            
    else:
        deactivate_rear_brakelights()
        deactivate_front_brakelights()
        release_brakes()
        
def update_reverse():
    reverse_sig = read_sbus_chanel(rudder_chanel)
    if reverse_sig < 300:
        activate_reverse()
        activate_rear_headlights()
        REVERSE = True
    else:
        deactivate_reverse()
        activate_front_headlights()
        REVERSE = False

def set_brush_power(power):
    #REMEMBER TO UNCOMMENT
    write_serial_b(power)

def set_drive_power(power):
    #REMEMBER TO UNCOMMENT
    write_serial_d(power)


def write_serial_d(power):
    output = "d"+ str(int(255*power))+"\n"
    out = output.encode('utf-8')
    try:
        ser.write(out)
        print("writing: ", output)
    except:
        print("serial disconected writing to drive")
        print("Reconnecting....")
        ser.close()
        serial_reconnect()
        
def write_serial_b(power):
    output = "b"+ str(int(255*power))+"\n"
    out = output.encode('utf-8')
    try:
        ser.write(out)
        print("writing: ", output)
    except:
        print("serial disconected writing to brush")
        print("Reconnecting....")
        ser.close()
        serial_reconnect()
    
def initialize_robot():
    deactivate_reverse()
    deactivate_brush_power()
    deactivate_drive_power()
    activate_emergency_light()
    stop_linear()
    set_brush_power(0.0)
    set_drive_power(0.0)
    deactivate_horn()
    activate_front_headlights()
    release_brakes()
    



    
def chooo():
    d_a = False
    start = time.time()
    while time.time() - start < 0.2 and demo_running:
        if d_a == False:
            activate_horn()
            d_a = True
    
    d_a = False
    start = time.time()
    while time.time() - start < 0.2 and demo_running:
        if d_a == False:
            deactivate_horn()
            d_a = True
    d_a = False
    start = time.time()
    while time.time() - start < 0.3 and demo_running:
        if d_a == False:
            activate_horn()   
            d_a = True
    deactivate_horn()

def state_1():
    start = time.time()
    # keyboard.add_hotkey('0', kill_demo)
    print("BEGINGIN STATE 1")
    # Lower Brushes
    if demo_running:
        lin_lowering = False
        while time.time() - start < 2 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if lin_lowering == False:
                lower_linear()
                lin_lowering = True
    stop_linear()
    # enable brush contactor
    if demo_running:
        start = time.time()
        brushes_activated = False
        while time.time() - start < 0.1 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if brushes_activated == False: 
                activate_brush_power()
                brushes_activated = True
    # Spin Up brushes
    set_brush_power(1.0)
    
    globals().update(State  = 2)
    globals().update(demo_running = True)
    print("end of 1 STATE:    ", State)
    
def state_2():
    
    print("BEGINGIN STATE 2")
    # Activate Drive Contactor
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 0.1 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                activate_drive_power()
                d_a = True
    # disengage brakes
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 2.5 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                release_brakes()
                d_a = True
    stop_brakes()
    # Horn
    if demo_running:
        chooo()
    # Drive Forward
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 3 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                set_drive_power(0.25)
                d_a = True
    
    # Stop Driving And apply brakes
    set_drive_power(0)
    deactivate_drive_power()
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 3 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                activate_brakes()
                activate_front_brakelights()
                d_a = True
    deactivate_front_brakelights()
    stop_brakes()
    
    # stop brushes and raise 
    
    set_brush_power(0)
    deactivate_brush_power()
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 3 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                raise_linear()
                d_a = True
    stop_linear()
    globals().update(State  = 3)
    globals().update(demo_running = True)
    print("end of 2 STATE:    ", State)
    
def state_3():
    # keyboard.add_hotkey('0', kill_demo)
    print("BEGINGIN STATE 3")
    # Flip Head Lights and reverse
    activate_rear_headlights()
    activate_reverse()
    
    # lower brushes
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 2.5 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                lower_linear()
                d_a = True
    stop_linear()
    
    
    # Start Brushes 
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 0.1 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                activate_brush_power()
                d_a = True
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 5 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                set_brush_power(1.0)
                d_a = True
    
    # Deactivate Brakes
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 2 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                release_brakes()
                d_a = True
    
    # horn
    if demo_running:
        chooo()
    
    # drive backwards
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 0.1 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                activate_drive_power()
                d_a = True
    
    set_drive_power(0.24)
    
    # wait for michael or 3 seconds
    if demo_running:
        start = time.time()
        michael = False
        while michael == False and (time.time() - start) < 3 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            check = get_rear_stereo()
            if check == 1:
                michael = True
    # apply brakes, stop driving, stop brushing
    activate_rear_brakelights()
    deactivate_brush_power()
    set_brush_power(0.0)
    deactivate_drive_power()
    set_drive_power(0)
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 2.5 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                activate_brakes()
                d_a = True
    stop_brakes()
    if demo_running:
        d_a = False
        start = time.time()
        while time.time() - start < 2.5 and demo_running:
            if keyboard.is_pressed('0'):
                kill_demo()
            if d_a == False:
                raise_linear()
                d_a = True
    globals().update(State  = 4)
    globals().update(demo_running = True)
    print("end of 3 STATE:    ", State)
    
  

def reset_demo():
    # STOPPING DEMO
    globals().update(demo_running = False)
    print("STOPPING DEMO")
    print("WAITING TO RESTART")
    globals().update(State  = 1)
    keyboard.unhook_all_hotkeys()
    demo()
    
def kill_demo():
    globals().update(demo_running = False)
    print("$$$$$$$$$$$$$$$ KILL DEMO $$$$$$$$$$$$$$$$$$$$$")
    print("DEMO IS RUNNING ", demo_running)
    initialize_robot()
    # reset_demo()

    
def begin_state():
    if State == 1:
        state_1()
    elif State == 2:
        state_2()
    elif State == 3:
        state_3()
    elif State == 4:
        globals().update(State = 1)
    
def demo():
    globals().update(demo_running = True)
    initialize_robot()
    keyboard.add_hotkey('9', begin_state)
    keyboard.wait('esc')
    
keyboard.add_hotkey('0', kill_demo)
release_brakes()
time.sleep(2)
demo()

