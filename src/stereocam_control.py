import time
import pigpio

pi = pigpio.pi()

REAR_STEREO = 17
FRONT_STEREO = 27

pi.set_mode(REAR_STEREO , pigpio.INPUT)
pi.set_mode(FRONT_STEREO , pigpio.INPUT)

pi.set_pull_up_down(REAR_STEREO, pigpio.PUD_DOWN)
pi.set_pull_up_down(FRONT_STEREO, pigpio.PUD_DOWN)

def get_front_stereo():
    read = pi.read(FRONT_STEREO)
    print("FRONT STEREO READ: ", read)
    return read

def get_rear_stereo():
    read = pi.read(REAR_STEREO)
    print("REAR STEREO READ: ", read)
    return read