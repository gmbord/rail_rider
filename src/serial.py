import serial
import time

ser = serial.Serial("/dev/ttyACM0", 115200, timeout=1)

# Reset the Arduino's line. This is key to getting the write to work.
# Without it, the first few writes don't work.
# Clear DTR, wait one second, flush input, then set DTR.
# Without this, the first write fails.
# This trick was learned from:
# https://github.com/miguelasd688/4-legged-robot-model

ser.setDTR(False)
time.sleep(1)
ser.flushInput()
ser.setDTR(True)
time.sleep(2)

while True:

	print('Telling the Arduino to start blinking...')
	ser.write(b'1')

	# read to get the acknowledgement from the Arduino
	while True:
		ack = ser.read()
		if ack == b'A':
			break
	print('Arduino sent back %s' % ack)

	time.sleep(2)

	print('Telling the Arduino to stop blinking...')
	ser.write(b'0')

	# read to get the acknowledgement from the Arduino
	while True:
		ack = ser.read()
		if ack == b'A':
			break
	print('Arduino sent back %s' % ack)

	time.sleep(2)
