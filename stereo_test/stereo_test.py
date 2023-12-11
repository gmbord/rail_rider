import time
import pigpio

pi = pigpio.pi()

STEREO_B = 17
STEREO_F = 27

pi.set_mode(STEREO_B, pigpio.INPUT)
pi.set_mode(STEREO_F, pigpio.INPUT)

pi.set_pull_up_down(STEREO_B, pigpio.PUD_DOWN)
pi.set_pull_up_down(STEREO_F, pigpio.PUD_DOWN)

while True:
    if pi.read(STEREO_B):
        print("BACK IN DA OBSTACLE")

    if pi.read(STEREO_F):
        print("OBSTACLE IN DA FRONT")

    time.sleep(0.1)
