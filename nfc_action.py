import os
from rfid_map import map_rfid_to_spotify_url
import git
from sonos import play_spotify_link


def nfc_action(id):
    if id == 228186622311:
        print("Perform git pull action")
        g = git.cmd.Git('./')
        g.pull()
    else:
        result = map_rfid_to_spotify_url(id)
        if result:
            play_spotify_link(result, os.environ.get('SONOS_DEVICE_IP'))
        else:
            print("No Spotify link found for id: " + str(id))
