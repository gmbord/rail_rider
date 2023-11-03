import time
import pigpio

DRIVE = 18
BRUSH_L = 12
BRUSH_R = 13

pi = pigpio.pi()
pi.set_PWM_dutycycle(DRIVE, 0)
pi.set_PWM_dutycycle(BRUSH_L, 0)
pi.set_PWM_dutycycle(BRUSH_R, 0)

    
def set_drive_speed(speed):
    pi.set_PWM_dutycycle(DRIVE, speed)
    print("DRIVE SPEED SET TO: ", (speed))
    
def set_brush_speed(speed):
    pi.set_PWM_dutycycle(BRUSH_L, speed)
    pi.set_PWM_dutycycle(BRUSH_R, speed)
    print("BRUSH SPEED SET TO: ", (speed))