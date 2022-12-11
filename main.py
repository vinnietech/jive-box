#!/usr/bin/env python3

from nfc_reader import read_nfc
from touch_buttons import listen_to_touch_buttons


def main():
    read_nfc()
    listen_to_touch_buttons()

if __name__ == "__main__":
    main()