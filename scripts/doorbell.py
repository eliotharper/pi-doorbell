#!/usr/bin/env python3
import signal
import sys
import os
import requests
import json
import RPi.GPIO as GPIO
BUTTON_GPIO = 23
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_pressed_callback(channel):
    print("button pressed")
    url = 'http://127.0.0.1:3000/cast/'
    body1 = {'device': 'Downstairs Wifi', 'source': '/home/pi/Music/doorbell.mp3', 'type':'local'}
    body2 = {'device': 'Upstairs Wifi', 'source': '/home/pi/Music/doorbell.mp3', 'type':'local'}
    headers = {'Content-Type': 'application/json'}
    response1 = requests.post(url, data=json.dumps(body1), headers=headers)
    response2 = requests.post(url, data=json.dumps(body2), headers=headers)
    print(response1.text)
    print(response2.text)
if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.FALLING,callback=button_pressed_callback, bouncetime=50)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()