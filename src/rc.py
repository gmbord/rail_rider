import read_sbus_from_GPIO

SBUS_PIN = 4 #pin where sbus wire is plugged in, BCM numbering

reader = read_sbus_from_GPIO.SbusReader(SBUS_PIN)
reader.begin_listen()

def display_sbus():
    reader.display_latest_packet()
    
def read_sbus_chanel(chanel):
    return reader.translate_latest_packet()[chanel-1]

def sbus_connected():
    return reader.is_connected()