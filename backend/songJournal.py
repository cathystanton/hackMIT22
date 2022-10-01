import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

import os

# setup for Spotify Web API
# hardcoded for demo
os.environ['SPOTIPY_CLIENT_ID'] = '705f9d56de324473972b2ac2c7368a93'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'f502cba5baf442dbbc662dc778be76dc'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())


birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
results = spotify.current_user_recently_played(10)
albums = results['items']
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])

