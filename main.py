#!/usr/bin/env python3
from sonos import play_spotify_link
import os


def main():
    play_spotify_link("https://open.spotify.com/album/2Y9IRtehByVkegoD7TcLfi?si=Y4928Qu-TOic5gDLiZoeEw", os.environ.get('SONOS_DEVICE_IP'))

if __name__ == "__main__":
    main()