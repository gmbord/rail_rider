import time
import pigpio

pi = pigpio.pi()

LEFT1 = 5
LEFT2 = 6
RIGHT1 = 17
RIGHT2 = 27

pi.set_mode(LEFT1, pigpio.OUTPUT)
pi.set_mode(LEFT2, pigpio.OUTPUT)
pi.set_mode(RIGHT1, pigpio.OUTPUT)
pi.set_mode(RIGHT2, pigpio.OUTPUT)
pi.write(LEFT1, 0)
pi.write(LEFT2, 0)
pi.write(RIGHT1, 0)
pi.write(RIGHT2, 0)

def raise_linear():
    pi.write(LEFT1, 0)
    pi.write(LEFT2, 1)
    pi.write(RIGHT1, 1)
    pi.write(RIGHT2, 0)
    print("RAISING LINEAR ACTUATORS")
    
def lower_linear():
    pi.write(LEFT1, 1)
    pi.write(LEFT2, 0)
    pi.write(RIGHT1, 0)
    pi.write(RIGHT2, 1)
    print("LOWERING LINEAR ACTUATORS")
    
def stop_linear():
    pi.write(LEFT1, 0)
    pi.write(LEFT2, 0)
    pi.write(RIGHT1, 0)
    pi.write(RIGHT2, 0)
    print("STOPPING LINEAR ACTUATORS")