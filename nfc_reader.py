import time
from mfrc522 import SimpleMFRC522

from nfc_action import nfc_action


def read_nfc():
    reader = SimpleMFRC522()
    print("Waiting for NFC read")

    while True:
        id, text = reader.read_no_block()
        if id is not None:
            print("NFC read ID:", id)
            nfc_action(id)
            time.sleep(1)
