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

        
