import time
import pigpio

pi = pigpio.pi()

LIGHT = 21

pi.set_mode(LIGHT , pigpio.OUTPUT)

pi.write(LIGHT , 0)
print("DEACTIVATING EMERGENCY LIGHT")

def activate_emergency_light():
    pi.write(LIGHT , 1)
    print("ACTIVATING EMERGENCY LIGHT")
    
def deactivate_emergency_light():
    pi.write(LIGHT, 0)
    print("DEACTIVATING EMERGENCY POWER")