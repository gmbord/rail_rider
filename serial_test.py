
"""
serial_usb_simple.py  Demo that communicates over USB using serial I/O
from a Raspberry Pi to an Arduino.

To show that it work, this writes a '1' to the Arduino which then 
blinks the builtin LED on and off. The Arduino also sends back an 'A'
to acknowledge that it got the message. This does a read() to get
the 'A', demonstrating that reading also works. Two seconds later,
this writes a '0' to the Arduino which then stops the blinking.
The Arduino again sends back an 'A' to acknowledge that it got the
message and this reads the 'A'.

This was tested between a Raspberry Pi 3B (running Raspbian) and
an Arduino Mega 2560 and also between an NVIDIA Jetson TX1 (running 
Ubuntu) and the same Arduino.
"""

import serial
import time

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)

# Reset the Arduino's line. This is key to getting the write to work.
# Without it, the first few writes don't work.
# Clear DTR, wait one second, flush input, then set DTR.
# Without this, the first write fails.
# This trick was learned from:
# https://github.com/miguelasd688/4-legged-robot-model



while True:

	print('Telling the Arduino to start blinking...')
	ser.write(b'balls\n')
	line = ser.readline().decode('utf-8').rstrip()
	print(line)
	time.sleep(0.5)
	ser.write(b'150\n')
	line = ser.readline().decode('utf-8').rstrip()
	print(line)
	time.sleep(0.5)
 

	# # read to get the acknowledgement from the Arduino
	# while True:
	# 	ack = ser.read()
	# 	if ack == b'A':
	# 		break
	# print('Arduino sent back %s' % ack)

	# time.sleep(2)

	# print('Telling the Arduino to stop blinking...')
	# ser.write(b'0')

	# # read to get the acknowledgement from the Arduino
	# while True:
	# 	ack = ser.read()
	# 	if ack == b'A':
	# 		break
	# print('Arduino sent back %s' % ack)

	# time.sleep(2)
