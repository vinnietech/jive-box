import yaml

def map_rfid_to_spotify_url(id):
    stream = open("spotify_dict.yaml", 'r')
    dictionary = yaml.load(stream, Loader=yaml.Loader)
    for key, value in dictionary.items():
        if int(key) == id:
            return value