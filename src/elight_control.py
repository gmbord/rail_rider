import time
import pigpio

pi = pigpio.pi()

LIGHT = 21
HORN = 20

pi.set_mode(LIGHT , pigpio.OUTPUT)
pi.set_mode(HORN , pigpio.OUTPUT)

pi.write(LIGHT , 0)
print("DEACTIVATING EMERGENCY LIGHT")
pi.write(HORN , 0)
print("DEACTIVATING HORN")

def activate_emergency_light():
    pi.write(LIGHT , 1)
    # print("ACTIVATING EMERGENCY LIGHT")
    
def deactivate_emergency_light():
    pi.write(LIGHT, 0)
    # print("DEACTIVATING EMERGENCY POWER")
    
def activate_horn():
    pi.write(HORN, 1)
    print("Activating Horn")
    
def deactivate_horn():
    pi.write(HORN, 0)
    print("Deactivating Horn")