import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522


def read_nfc():
    reader = SimpleMFRC522()
    try:
        print("Waiting for NFC read")
        id = reader.read()[0]
        print("The ID for this card is:", id)

    finally:
        GPIO.cleanup()
