import sys
sys.path.append("src")
sys.path.append("/home/redpi/code/rail_rider/src")
sys.path.append("/home/redpi/.local/lib/pyhton3.11/site-packages")



import time
import RPi.GPIO as GPIO
from rc import *
from motor_control import *
from linear_control import *
from contactor_control import *
from elight_control import *
import keyboard
import serial

try:
    ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
    time.sleep(1)
except:
    serial_reconnect()





Drive_Armed = False
Brush_Armed = False

Frames_Dropped = 0

drive_armed_chanel = 6 # Switch 2, LOW: 192, High: 1792 
brush_armed_chanel = 7 # Switch 3, LOW: 192, High: 1792 
drive_trotle_chanel = 1 # Throttle Stick, LOW: 192, HIOH: 1792
brush_trotle_chanel = 8 # Switch 4, LOW: 192, MID: 992, HIGH: 1792
linear_chanel = 5 #Switch 1, LOW: 192, MID: 992, HIGH: 1792
rudder_chanel = 4 # Throttle stick x axis
elevator_chanel = 3 # elevator for horn

drive_throttle = 0
brush_throttle = 0
elight_on = False
linear_state = 0

def inc_drive_throttle():
    if Drive_Armed:
        if drive_throttle < 100:
            globals().update(drive_throttle = drive_throttle+1)
        update_drive(drive_throttle)
        print("Drive Throttle", drive_throttle)
    else:
        print("Drive Disarmed")
    
def dec_drive_throttle():
    if Drive_Armed:
        if drive_throttle > 0:
            globals().update(drive_throttle = drive_throttle-1)
        update_drive(drive_throttle)
        print("Drive Throttle", drive_throttle)
    else:
        print("Drive Disarmed")
        
def drive_throttle_zero():
    if Drive_Armed:
        if drive_throttle > 0:
            globals().update(drive_throttle = 0)
        update_drive(drive_throttle)
        print("Drive Throttle", drive_throttle)
    else:
        print("Drive Disarmed")
    
def kill_drive_throttle():
    globals().update(drive_throttle = 0)
    globals().update(Drive_Armed = False)
    update_drive(drive_throttle)
    deactivate_drive_power()
    print("Drive Throttle", drive_throttle)
    print("Drive Disarmed")
    
def inc_brush_throttle():
    if Brush_Armed:
        if brush_throttle < 50:
            globals().update(brush_throttle = brush_throttle+1)
        update_brush(brush_throttle)
        print("Brush Throttle", brush_throttle)
    else:
        print("Brush Disarmed")
    
def dec_brush_throttle():
    if Brush_Armed:
        if brush_throttle > 0:
            globals().update(brush_throttle = brush_throttle-1)
        update_brush(brush_throttle)
        print("Brush Throttle" , brush_throttle)
    else:
        print("Brush Disarmed")
        
def brush_throttle_zero():
    if Brush_Armed:
        if brush_throttle > 0:
            globals().update(brush_throttle = 0)
        update_brush(brush_throttle)
        print("Brush Throttle" , brush_throttle)
    else:
        print("Brush Disarmed")
    
def kill_brush_throttle():
    globals().update(brush_throttle = 0)
    globals().update(Brush_Armed = False)
    update_brush(brush_throttle)
    deactivate_brush_power()
    print("Brush Throttle", brush_throttle)
    print("Brush Disarmed")
    
def arm_brush():
    globals().update(Brush_Armed = True)
    activate_brush_power()
    print("Brush Armed")
    
def arm_drive():
    globals().update(Drive_Armed = True)
    activate_drive_power()
    print("Drive Armed")
    
def turn_elight_on():
    globals().update(elight_on = True)
    update_elight(elight_on)
    print("Emergency Light On")
    
def turn_elight_off():
    globals().update(elight_on = False)
    update_elight(elight_on)
    print("Emergency Light Off")
    
def set_linear_up():
    globals().update(linear_state = 1)
    update_linear(linear_state)
    print("Linear State: Raising")
    
def set_linear_down():
    globals().update(linear_state = -1)
    update_linear(linear_state)
    print("Linear State: Lowering")
    
def set_linear_stop():
    globals().update(linear_state = 0)
    update_linear(linear_state)
    print("Linear State: Stopping")
    
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
    write_serial_d(power)
    # output = "d" + str(int(255*power))+"\n"
    # #out = bytes(output, 'utf-8')
    # out = output.encode('utf-8')
    # try:
    #     ser.write(out)
    # except Error as e:
    #     print(e)
    #     print(out)
    # line = ser.readline().decode('utf-8').rstrip()
    # print("Setting Drive Speed: ", line)
    # set_drive_speed(power)
    
def update_drive_zero():
    power = 0
    write_serial_d(power)
    # output = "d"+ str(int(255*power))+"\n"
    # #out = bytes(output, 'utf-8')
    # out = output.encode('utf-8')
    # try:
    #     ser.write(out)
    # except Error as e:
    #     print(e)
    #     print(out)
    # line = ser.readline().decode('utf-8').rstrip()
    # print("Setting Drive Speed: ", line)

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
    write_serial_b(power)
    # output = "b" + str(int(255*power))+"\n"
    # #out = bytes(output, 'utf-8')
    # out = output.encode('utf-8')
    # try:
    #     ser.write(out)
    # except Error as e:
    #     print(e)
    #     print(out)
    # line = ser.readline().decode('utf-8').rstrip()
    # print("Setting Drive Speed: ", line)
        
    # set_brush_speed(power)
def update_brush_zero():
    power = 0
    write_serial_b(power)
    # output = "b" + str(int(255*power))+"\n"
    # #out = bytes(output, 'utf-8')
    # out = output.encode('utf-8')
    # try:
    #     ser.write(out)
    # except Error as e:
    #     print(e)
    #     print(out)
    # line = ser.readline().decode('utf-8').rstrip()
    # print("Setting Drive Speed: ", line)
    
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
        
def update_reverse():
    reverse_sig = read_sbus_chanel(rudder_chanel)
    if reverse_sig < 300:
        activate_reverse()
    else:
        deactivate_reverse()
    
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
        
        
        
def read_serial():
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    
def initialize_robot():
    deactivate_brush_power()
    deactivate_drive_power()
    activate_emergency_light()
    stop_linear()
    update_brush_zero()
    update_drive_zero()

def main_control_loop():
    # while True:
    #     for i in range(255):
    #         update_drive(i)
    #         update_brush(i)
    #         # update_drive_zero()
    #         # update_brush_zero()
            
    #         time.sleep(0.05)
    #     time.sleep(0.5)
        
    while True:
        sbus_con = sbus_connected()
        if sbus_con:
            globals().update(Frames_Dropped  = 0)
            
            update_armed()
            update_reverse()
            if Drive_Armed:
                activate_drive_power()
                update_drive()
            else:
                deactivate_drive_power()
                update_drive_zero()
            if Brush_Armed:
                activate_brush_power()
                update_brush()
            else:
                deactivate_brush_power()
                update_brush_zero()
            update_linear()
            update_horn()
            print("SBUS IS CONNECTED: ", sbus_con)
            
        else:
            globals().update(Frames_Dropped  = Frames_Dropped + 1)
            if Frames_Dropped > 50:
                initialize_robot()
                globals().update(Drive_Armed = False)
                globals().update(Brush_Armed = False)
        time.sleep(0.05)
        print("")
        print("*********************************************")
        
        
    # keyboard.add_hotkey('w', inc_drive_throttle)
    # keyboard.add_hotkey('q', dec_drive_throttle)
    # keyboard.add_hotkey('shift + q', drive_throttle_zero)
    # keyboard.add_hotkey('x', kill_drive_throttle)
    # keyboard.add_hotkey('s', inc_brush_throttle)
    # keyboard.add_hotkey('a', dec_brush_throttle)
    # keyboard.add_hotkey('shift + a', brush_throttle_zero)
    # keyboard.add_hotkey('z', kill_brush_throttle)
    # keyboard.add_hotkey('shift + z', arm_brush)
    # keyboard.add_hotkey('shift + x', arm_drive)
    # keyboard.add_hotkey('l', turn_elight_on)
    # keyboard.add_hotkey('k', turn_elight_off)
    # keyboard.add_hotkey('i', set_linear_down)
    # keyboard.add_hotkey('o', set_linear_stop)
    # keyboard.add_hotkey('p', set_linear_up)
    
    # keyboard.wait('esc')  
    


initialize_robot()
main_control_loop()
