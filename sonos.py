from soco import SoCo
from soco.plugins.sharelink import ShareLinkPlugin
from soco import discover

def play_spotify_link(share_link, device_ip):

    print(f'Playing {share_link} on Sonos device #{device_ip}')

    device = SoCo(device_ip)

    device.stop()
    device.clear_queue()
    sharelink = ShareLinkPlugin(device)
    sharelink.add_share_link_to_queue(share_link)
    device.play_from_queue(index=0)


def list_devices():
    for zone in discover():
        print(zone.player_name)