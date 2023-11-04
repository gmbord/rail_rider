import read_sbus_from_GPIO

SBUS_PIN = 4 #pin where sbus wire is plugged in, BCM numbering

reader = read_sbus_from_GPIO.SbusReader(SBUS_PIN)
reader.begin_listen()

def test_func():
    reader.display_latest_packet()