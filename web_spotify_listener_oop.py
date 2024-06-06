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

class my_playlist_handler:
        
        def __init__(self):
            self.client_id= ''  # Get your client id from Spotify developer dashboard
            self.client_secret = ''  # Get your client secret from Spotify developer dashboard
            self.redirect_uri = 'http://google.com/'
            self.scope = 'playlist-modify-public playlist-modify-private ugc-image-upload'
            self.playlist_id = ''
            self.username = ''           
    

            self.sp_oauth = SpotifyOAuth(client_id=self.client_id, client_secret=self.client_secret, redirect_uri=self.redirect_uri, scope=self.scope, show_dialog=True)
            self.sp = spotipy.Spotify(auth_manager=self.sp_oauth) 

        

class web_listener(my_playlist_handler):
        
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
        



        
        
