from pytube import Playlist,Search
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import shutil
import os

CLIENT_ID = '0433e3d91ac54cd5b16f81ed87993bac'
CLIENT_SECRET = "b17dcbc365b8495cb06622a1e224a505"
PLAYLIST_LINK = url = input("url: ")

CLIENT_CREDENTIALS_MANAGER = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=CLIENT_CREDENTIALS_MANAGER)

def get_tracks():
    tracks = []
    for track in sp.playlist_tracks(PLAYLIST_LINK)["items"]:
        result = track["track"]["name"]+" - "+track["track"]["artists"][0]["name"]
        tracks.append(result)
    return tracks

title = sp.playlist(PLAYLIST_LINK)["name"]
tracks = get_tracks()

d_tracks = []
for track in tracks:
    d_tracks.append(Search(track + " lyrics").results[0])

def sanitize(ch):
    chx = ""
    for i in range(len(ch)):
        if "A" <= ch[i].upper() <= "Z" or ch[i]=="-" or ch[i]==" " or "0" <= ch[i].upper() <= "9":
            chx += ch[i]
    return chx
output_pt = input("give url 'C:/Users/dir/' :")+title
os.makedirs(output_pt)
for video, video_title in zip(d_tracks,tracks):
    stream = video.streams.filter(only_audio=True,  abr='128kbps').first()
    filename = sanitize(video_title)
    stream.download(filename=f"{filename}.mp3",output_path=output_pt)
shutil.make_archive(output_pt,'zip',output_pt)
