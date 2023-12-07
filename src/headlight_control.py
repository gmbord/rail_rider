import time
import pigpio

pi = pigpio.pi()

HEADLIGHT_R = 12
HEADLIGHT_F = 21
BRAKELIGHT_R = 13
BRAKELIGHT_F = 14

pi.set_mode(HEADLIGHT_R , pigpio.OUTPUT)
pi.set_mode(HEADLIGHT_F , pigpio.OUTPUT)
pi.set_mode(BRAKELIGHT_R , pigpio.OUTPUT)
pi.set_mode(BRAKELIGHT_F , pigpio.OUTPUT)


pi.write(HEADLIGHT_F , 1)
print("ACTIVATING FRONT HEAD LIGHT")
pi.write(HEADLIGHT_R , 0)
print("DEACTIVATING REAR HEAD LIGHT")
pi.write(BRAKELIGHT_R, 0)
print("DEACTIVATING REAR BRAKE LIGHT")
pi.write(BRAKELIGHT_F, 0)
print("DEACTIVATING FRONT BRAKE LIGHT")

def activate_front_headlights():
    pi.write(HEADLIGHT_F , 1)
    print("ACTIVATING FRONT HEAD LIGHT")
    pi.write(HEADLIGHT_R , 0)
    print("DEACTIVATING REAR HEAD LIGHT")
    
def activate_rear_headlights():
    pi.write(HEADLIGHT_F , 0)
    print("DEACTIVATING FRONT HEAD LIGHT")
    pi.write(HEADLIGHT_R , 1)
    print("ACTIVATING REAR HEAD LIGHT")
    
def deactivate_headlights():
    pi.write(HEADLIGHT_F , 0)
    print("DEACTIVATING FRONT HEAD LIGHT")
    pi.write(HEADLIGHT_R , 0)
    print("DEACTIVATING REAR HEAD LIGHT")
    
def activate_front_brakelights():
    pi.write(BRAKELIGHT_F, 1)
    print("ACTIVATING FRONT BRAKE LIGHT")
    
def deactivate_front_brakelights():
    pi.write(BRAKELIGHT_F, 0)
    print("DEACTIVATING FRONT BRAKE LIGHT")
    
def activate_rear_brakelights():
    pi.write(BRAKELIGHT_R, 1)
    print("ACTIVATING REAR BRAKE LIGHT")
    
def deactivate_rear_brakelights():
    pi.write(BRAKELIGHT_R, 0)
    print("DEACTIVATING REAR BRAKE LIGHT")