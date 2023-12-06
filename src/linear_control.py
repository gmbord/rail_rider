import time
import pigpio

pi = pigpio.pi()

DIR1 = 5
DIR2 = 6
BRAKE1 = 2
BRAKE2 = 3


pi.set_mode(DIR1, pigpio.OUTPUT)
pi.set_mode(DIR2, pigpio.OUTPUT)
pi.set_mode(BRAKE1, pigpio.OUTPUT)
pi.set_mode(BRAKE2, pigpio.OUTPUT)

pi.write(DIR1, 0)
pi.write(DIR2, 0)
pi.write(BRAKE1, 0)
pi.write(BRAKE2, 0)

def raise_linear():
    pi.write(DIR1, 1)
    pi.write(DIR2, 0)
    print("RAISING LINEAR ACTUATORS")
    
def lower_linear():
    pi.write(DIR1, 0)
    pi.write(DIR2, 1)
    print("LOWERING LINEAR ACTUATORS")
    
def stop_linear():
    pi.write(DIR1, 0)
    pi.write(DIR2, 0)
    print("STOPPING LINEAR ACTUATORS")
    
def release_brakes():
    pi.write(BRAKE1, 1)
    pi.write(BRAKE2, 0)
    print("RELEASING BRAKES")
    
def activate_brakes():
    pi.write(BRAKE1, 0)
    pi.write(BRAKE2, 1)
    print("ACTIVATING BRAKES")

def stop_brakes():
    pi.write(BRAKE1, 0)
    pi.write(BRAKE2, 0)
    print("STOPPING BRAKES")