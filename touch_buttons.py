import os
import time
import RPi.GPIO as GPIO

import sonos

TOUCH_SLEEP_TIME = 0.5

PREVIOUS_TOUCH_PIN = 4
PAUZE_PLAY_TOUCH_PIN = 17
NEXT_TOUCH_PIN = 27


def touch_detect(pin):
    touch = GPIO.input(pin)
    return touch

def listen_to_touch_buttons():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PREVIOUS_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PAUZE_PLAY_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(NEXT_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if touch_detect(PREVIOUS_TOUCH_PIN):
            sonos.play_previous(os.environ.get('SONOS_DEVICE_IP'))
            time.sleep(TOUCH_SLEEP_TIME)

    while True:
        if touch_detect(NEXT_TOUCH_PIN):
            sonos.play_next(os.environ.get('SONOS_DEVICE_IP'))
            time.sleep(TOUCH_SLEEP_TIME)

    while True:
        if touch_detect(PAUZE_PLAY_TOUCH_PIN):
            sonos.toggle_play_pause(os.environ.get('SONOS_DEVICE_IP'))
            time.sleep(TOUCH_SLEEP_TIME)
