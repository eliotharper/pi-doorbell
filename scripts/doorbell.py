#!/usr/bin/env python3
import signal
import sys
import os
import RPi.GPIO as GPIO
BUTTON_GPIO = 23
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_pressed_callback(channel):
    os.system("nohup sh /home/pi/Scripts/doorbell.sh &")
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,callback=button_pressed_callback, bouncetime=100)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()