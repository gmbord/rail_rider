import time
import pigpio

#Max 3.5 V -> 1
#Min 0.875 V -> 0.265


REVERSE = 26

pi = pigpio.pi()

pi.set_mode(REVERSE , pigpio.OUTPUT)
pi.write(REVERSE, 0)
    
def activate_reverse():
    pi.write(REVERSE, 0)
    print("Activating Reverse")
    
def deactivate_reverse():
    pi.write(REVERSE, 1)
    print("dectivating Reverse")