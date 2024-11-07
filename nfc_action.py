import os
from rfid_map import map_rfid_to_spotify_url
import git

from slack_notification import send_missing_id_notification
from sonos import play_spotify_link


def nfc_action(id):
    if id == os.environ.get('GIT_PULL_NFC_ID'):
        print("Perform git pull action")
        g = git.cmd.Git(os.path.dirname(os.path.abspath(__file__)))
        g.pull()
    else:
        result = map_rfid_to_spotify_url(id)
        if result:
            play_spotify_link(result, os.environ.get('SONOS_DEVICE_IP'))
        else:
            print("No Spotify link found for id: " + str(id))
            send_missing_id_notification(id)