import time
import pigpio

#Max 3.3 V -> 1
#Min 0.875 V -> 0.265

DRIVE = 18
BRUSH_L = 12
BRUSH_R = 13

pi = pigpio.pi()
pi.set_mode(DRIVE, pigpio.OUTPUT)
pi.set_mode(BRUSH_L, pigpio.OUTPUT)
pi.set_mode(BRUSH_R, pigpio.OUTPUT)
pi.write(DRIVE, 0)
pi.write(BRUSH_L, 0)
pi.write(BRUSH_R, 0)

    
def set_drive_speed(speed):
    speed = (speed * 0.735) + 0.265
    if speed > 1:
        speed = 1
    if speed < 0.265:
        speed = 0.265
    pi.write(DRIVE, speed)
    print("DRIVE SPEED SET TO: ", (speed))
    
def set_brush_speed(speed):
    speed = (speed * 0.735) + 0.265
    if speed > 1:
        speed = 1
    if speed < 0.265:
        speed = 0.265
    pi.write(BRUSH_L, speed)
    pi.write(BRUSH_R, speed)
    print("BRUSH SPEED SET TO: ", (speed))