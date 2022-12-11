#!/usr/bin/env python3

from nfc_reader import read_nfc
from sonos_touch_controls.touch_buttons import listen_to_touch_buttons


def main():
    listen_to_touch_buttons()

if __name__ == "__main__":
    main()