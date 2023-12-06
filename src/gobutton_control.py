import time
import pigpio

pi = pigpio.pi()

BUTTON = 23

pi.set_mode(BUTTON , pigpio.INPUT)

pi.set_pull_up_down(BUTTON, pigpio.PUD_DOWN)

def get_go_button():
    read = pi.read(BUTTON)
    print("GO BUTTON READ: ", read)
    return read