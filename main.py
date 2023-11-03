import time
import RPi.GPIO as GPIO
from rc import *

while True:
    test_func()



# GPIO.setmode(GPIO.BOARD)
# GPIO.setup(13, GPIO.OUT)

# p = GPIO.PWM(13, 50)
# p.start(0)
# time.sleep(10)

# p.ChangeDutyCycle(3)