import time
import pigpio

#Max 3.5 V -> 1
#Min 0.875 V -> 0.265

DRIVE = 18
BRUSH_L = 12
BRUSH_R = 13

REVERSE = 26

pi = pigpio.pi()
pi.set_mode(DRIVE, pigpio.OUTPUT)
pi.set_mode(BRUSH_L, pigpio.OUTPUT)
pi.set_mode(BRUSH_R, pigpio.OUTPUT)
pi.set_mode(REVERSE , pigpio.OUTPUT)
# pi.set_PWM_frequency(DRIVE, 100)
# pi.set_PWM_frequency(BRUSH_L, 100)
# pi.set_PWM_frequency(BRUSH_R, 100)
print(pi.get_PWM_frequency(DRIVE))
pi.set_PWM_dutycycle(DRIVE, 0)
pi.set_PWM_dutycycle(BRUSH_L, 0)
pi.set_PWM_dutycycle(BRUSH_R, 0)
pi.write(REVERSE, 0)

    
def set_drive_speed(speed):
    speed = 255*speed
    if speed > 255:
        speed = 255
    if speed < 0:
        speed = 0
    pi.set_PWM_dutycycle(DRIVE, speed)
    print("DRIVE SPEED SET TO: ", (speed))
    
def set_brush_speed(speed):
    speed = 255*speed
    if speed > 255:
        speed = 255
    if speed < 0:
        speed = 0
    pi.set_PWM_dutycycle(BRUSH_L, speed)
    pi.set_PWM_dutycycle(BRUSH_R, speed)
    print("BRUSH SPEED SET TO: ", (speed))
    
def activate_reverse():
    pi.write(REVERSE, 1)
    print("Activating Reverse")
    
def deactivate_reverse():
    pi.write(REVERSE, 0)
    print("dectivating Reverse")