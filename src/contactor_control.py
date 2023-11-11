import time
import pigpio

pi = pigpio.pi()

DRIVE = 22
BRUSH = 19


pi.set_mode(DRIVE, pigpio.OUTPUT)
pi.set_mode(BRUSH, pigpio.OUTPUT)

pi.write(DRIVE, 0)
print("DEACTIVATING DRIVE POWER")
pi.write(BRUSH, 0)
print("DEACTIVATING DRIVE POWER")

def activate_drive_power():
    pi.write(DRIVE, 1)
    print("ACTIVATING DRIVE POWER")
    
def deactivate_drive_power():
    pi.write(DRIVE, 0)
    print("DEACTIVATING DRIVE POWER")
    
def activate_brush_power():
    pi.write(BRUSH, 1)
    print("ACTIVATING DRIVE POWER")
    
def deactivate_brush_power():
    pi.write(BRUSH, 0)
    print("DEACTIVATING DRIVE POWER")