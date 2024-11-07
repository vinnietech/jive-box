from soco import SoCo
from soco.plugins.sharelink import ShareLinkPlugin
from soco import discover

# we assume the there is a song playing and toggle with play is true initially
playing = True

def play_spotify_link(share_link, device_ip):

    print(f'Playing {share_link} on Sonos device #{device_ip}')

    device = SoCo(device_ip)

    device.stop()
    device.clear_queue()
    sharelink = ShareLinkPlugin(device)
    sharelink.add_share_link_to_queue(share_link)
    device.play_from_queue(index=0)


def play_previous(device_ip):
    print(f'Previous song for #{device_ip}')

    device = SoCo(device_ip)
    device.previous()

def play_next(device_ip):
    print(f'Next song for #{device_ip}')

    device = SoCo(device_ip)
    device.next()

def toggle_play_pause(device_ip):
    global playing
    print(f'Toggle play/pause for #{device_ip}')

    device = SoCo(device_ip)
    if playing:
        device.pause()
        playing = False
    else:
        device.play()
        playing = True

def list_devices():
    for zone in discover():
        print(zone.player_name)