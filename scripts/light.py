#!/usr/bin/env python3
import signal
import sys
import os
import requests
import json
import RPi.GPIO as GPIO
url = 'http://127.0.0.1:3000/assistant/'
headers = {'Content-Type': 'application/json'}
BUTTON_GPIO = 10
def signal_handler(sig, frame):
    GPIO.cleanup()
    sys.exit(0)
def button_callback(channel):  
    if GPIO.input(10): # port 10 == 1  
        print "Rising edge detected"
        body = {'command': 'turn on book nook', 'converse': False, 'user': 'dad'}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response.text)
    else: # port 10 != 1  
        print "Falling edge detected"
        body = {'command': 'turn off book nook', 'converse': False, 'user': 'dad'}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        print(response.text)
if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(BUTTON_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(BUTTON_GPIO, GPIO.BOTH, callback=button_callback, bouncetime=50)
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()