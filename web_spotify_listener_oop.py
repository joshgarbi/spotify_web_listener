#listen to https://listen.klove.com/ and add the song to a spotify playlist

import requests
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy import util
from bs4 import BeautifulSoup
import time
from lxml import html
import os
from spotipy.cache_handler import CacheHandler
import playlist_handler

class web_listener(playlist_handler.my_playlist_handler):
        
    def __init__(self):
        super().__init__()
        self.song_title_var = ''
        self.artist_name_var = ''
        self.url = ''
        self.name = ''
        self.initialize_state = False

    def initialize(self, song_title_var, artist_name_var, url, name):
        self.song_title_var = song_title_var
        self.artist_name_var = artist_name_var
        self.url = url
        self.name = name
        self.initialize_state = True
        #create a csv file with the name self.name
        file = open(self.name, 'w')
        file.write('spotify:track:TEMP' + '\n')
        
    def get_song(self):
        data = requests.get(self.url).json()
        song = data[self.song_title_var]
        artist = data[self.artist_name_var]
        if (self.initialize):
            self.song = song
            self.artist = artist
        else:
            return Exception("Initialize the class first")
    
    def get_spotify_uri(self, song, artist):
        #print(song, artist)
        result = self.sp.search(q=f'track:{song} artist:{artist}', limit=1, type='track')
        #print(result)
        try:
            uri = result['tracks']['items'][0]['uri']
            return uri
        except:
            return 'spotify:track:TEMP'
 
    def add_to_playlist(self, uri):
        with open(self.name, 'r') as file:
            songs = file.readlines()
        if uri + '\n' not in songs:
            with open(self.name, 'a') as file:
                file.write(uri + '\n')
                print('Song added to playlist')
        else:
            print('Song already in playlist')
        file.close()
        


    def main(self):
        song, artist = self.get_song()
        uri = self.get_spotify_uri(song, artist)
        self.add_to_playlist(uri)
        



        
        
