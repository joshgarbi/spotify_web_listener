import web_spotify_listener_oop



def main():
    client_id= 'cde9fef58daa4b1c9364d70ac96f1d55'  # Get your client id from Spotify developer dashboard
    client_secret = '9fcd500e0c0b477095bbf94ad00fb37e'  # Get your client secret from Spotify developer dashboard
    playlist_id = '4tkKGDu1LzNf8ULBtIMKfH'
    username = '09y27tdmjn0pofjcmru8qss8q'
    
    MyKloveListener = web_spotify_listener_oop.web_listener()
    
    MyKloveListener.initialize('songTitle', 'artistName', 'https://www.klove.com/api/next/getNowPlaying', 'klove_songs')
    
    MyKloveListener.get_song()
    uri = MyKloveListener.get_spotify_uri(MyKloveListener.song, MyKloveListener.artist)
    MyKloveListener.add_to_playlist(uri)

main()