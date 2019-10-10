import requests


API_KEY = '340917bab50c8af5fd783da640a58931'


def get_top_artist():
    url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettopartists&api_key={API_KEY}&format=json'
    top_50_artist = requests.get(url).json()
    return top_50_artist


def get_top_tracks():
    url = f'http://ws.audioscrobbler.com/2.0/?method=chart.gettoptracks&api_key={API_KEY}&format=json'
    top_50_tracks = requests.get(url).json()
    return top_50_tracks


def get_artist_info(artist_name):
    url = f'http://ws.audioscrobbler.com/2.0/?method=artist.getinfo&artist={artist_name}&api_key={API_KEY}&format=json'
    artist_info = requests.get(url).json()
    return artist_info


def get_album_info(artist_name, album_title):
    url = f'http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={API_KEY}&artist={artist_name}&album={album_title}&format=json'
    album_info = requests.get(url).json()
    return album_info


def get_track_info(artist_name, track_title):
    url = f'http://ws.audioscrobbler.com/2.0/?method=track.getInfo&api_key={API_KEY}&artist={artist_name}&track={track_title}&format=json'
    track_info = requests.get(url).json()
    return track_info


def preparing_message(source_message):
    message = []
    for artist in source_message:
        name = artist['name']
        listeners = artist['listeners']
        artist_url = artist['url']
        
        message.append(f'[{name}]({artist_url}), слушают {listeners}.\r\n')
    return '\r\n'.join(message)