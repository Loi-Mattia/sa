import spotipy
from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
from flask_restful import Resource , Api ,reqparse
from bson import json_util
from spotipy.oauth2 import SpotifyClientCredentials

import spotipy.util as util


app = Flask(_name_)

birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='c0b1eb0b7a7848eb8436567d5871b8c2', client_secret='33394ae9bebc434b8ad0ff3acfb11640'))

CORS(app)
api = Api(app)


@app.route('/')
def index():
    return ("ciao")


@app.route('/link')
def tab():
    results = spotify.artist_albums(birdy_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        resp = json_util.dumps(album)
    return Response(resp, mimetype='application/json')

@app.route('/outh')
def get_spotify_uri(self, song_name, artist):
    query = "https://api.spotify.com/v1/search".format(song_name, artist)

    response = requests.get(
        query,
        headers={
            "Content-type": "application/json",
            "Authorization": "Bearer {}".format(spotify_token)
        }
    )
    response_json = response.json()
    songs = response_json["tracks"]["items"]


    uri = songs[0]["uri"]
    
    resp = json_util.dumps(response_json)
    return Response(resp, mimetype='application/json')

if _name_ == '_main_':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)