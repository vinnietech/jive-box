import yaml
import os

ymlFile = os.path.dirname(os.path.abspath(__file__)) + "/spotify_dict.yaml"

def map_rfid_to_spotify_url(id):
    stream = open(ymlFile, 'r')
    dictionary = yaml.load(stream, Loader=yaml.Loader)
    for key, value in dictionary.items():
        if int(key) == id:
            return value