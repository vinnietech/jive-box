import os
import time
import RPi.GPIO as GPIO

import sonos

TOUCH_SLEEP_TIME = 1

PREVIOUS_TOUCH_PIN = 23
PAUZE_PLAY_TOUCH_PIN = 22
NEXT_TOUCH_PIN = 27



def touch_detect(pin):
    touch = GPIO.input(pin)
    return touch


def listen_to_touch_buttons():
    if not os.getenv("SONOS_DEVICE_IP"):
        raise ValueError("Environment variable SONOS_DEVICE_IP is not set.")

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PREVIOUS_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(PAUZE_PLAY_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(NEXT_TOUCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        if touch_detect(PREVIOUS_TOUCH_PIN):
            print("Previous touch detected")
            try:
                sonos.play_previous(os.environ.get('SONOS_DEVICE_IP'))
            except:
                print("Error playing previous song")
            time.sleep(TOUCH_SLEEP_TIME)

        if touch_detect(NEXT_TOUCH_PIN):
            print("Next touch detected")
            try:
                sonos.play_next(os.environ.get('SONOS_DEVICE_IP'))
            except:
                print("Error playing next song")
            time.sleep(TOUCH_SLEEP_TIME)

        if touch_detect(PAUZE_PLAY_TOUCH_PIN):
            print("Play/pause touch detected")
            try:
                sonos.toggle_play_pause(os.environ.get('SONOS_DEVICE_IP'))
            except:
                print("Error toggling play/pause")
            time.sleep(TOUCH_SLEEP_TIME)

        # add a small sleep to prevent using 100% of the CPU
        time.sleep(0.01)

listen_to_touch_buttons()