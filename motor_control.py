import time
import pigpio

DRIVE = 18
BRUSH_L = 12
BRUSH_R = 13

pi = pigpio.redpi()
pi.set_duty_cycle(DRIVE, 0)
pi.set_duty_cycle(BRUSH_L, 0)
pi.set_duty_cycle(BRUSH_R, 0)

    
def set_drive_speed(speed):
    pi.set_duty_cycle(DRIVE, speed)
    print("DRIVE SPEED SET TO: " + speed)
    
def set_brush_speed(speed):
    pi.set_duty_cycle(BRUSH_L, speed)
    pi.set_duty_cycle(BRUSH_R, speed)
    print("BRUSH SPEED SET TO: " + speed)