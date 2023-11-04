import time
import RPi.GPIO as GPIO
from src/rc import *
from src/motor_control import *



while True:
    test_func()
    set_drive_speed(0.2)
    set_brush_speed(0.2)
    time.sleep(1)


# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(13, GPIO.OUT)

# p = GPIO.PWM(13, 50)
# p.start(0)
# time.sleep(10)

# p.ChangeDutyCycle(3)
