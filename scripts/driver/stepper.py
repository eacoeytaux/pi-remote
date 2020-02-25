#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

# setup

last_dir_file = open(sys.argv[2], "r+")

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

control_pins = [7,11,13,15]

for pin in control_pins:
    GPIO.setup(pin, GPIO.OUT)

halfstep_seq_down = [
        [1,0,0,0],
	[1,1,0,0],
	[0,1,0,0],
	[0,1,1,0],
	[0,0,1,0],
	[0,0,1,1],
	[0,0,0,1],
	[1,0,0,1]
]
halfstep_seq_up = [
        [0,0,0,1],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0],
        [1,0,0,1]
]

def move(dir):
    for step in range(16):
        for halfstep in range(8):
            for pin in range(4):
                if dir == "up":
                    GPIO.output(control_pins[pin], halfstep_seq_up[halfstep][pin])
                elif dir == "down":
                    GPIO.output(control_pins[pin], halfstep_seq_down[halfstep][pin])
                time.sleep(0.001)

# functionality

dir = sys.argv[1]

if dir == "still":
    exit(0)

if dir != "up" and dir != "down":
    print("direction \"" + dir + "\" not supported")
    exit(1)

# build up tension
last_dir = last_dir_file.read()
if dir != last_dir:
    for i in range(8):
        move(dir)

move(dir);

GPIO.cleanup()

last_dir_file.seek(0)
last_dir_file.write(dir)
last_dir_file.truncate()
last_dir_file.close()

