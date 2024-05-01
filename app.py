import os
from flask import Flask
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import config

app = Flask(__name__)

@app.route("/")
def top_tracks(): 

    # Set up Spotify client credentials
    client_id = config.client_id
    client_secret = config.client_secret
    client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Fetch the top tracks https://open.spotify.com/playlist/37i9dQZEVXbMDoHDwVN2tF

    top_tracks = sp.playlist_tracks('37i9dQZEVXbMDoHDwVN2tF')['items']

    # Print the top track names and artists
    tracks = []
    a_track = {}

    for track in top_tracks:
        track_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        print(f"{track_name} - {artist_name}")
        a_track["track_name"] = track_name
        a_track["artist_name"] = artist_name
        tracks.append(a_track)

    # return top_tracks
    return tracks



    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))




