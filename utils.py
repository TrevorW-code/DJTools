from fileinput import filename
import mutagen
import csv
import os
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
import json
import pdb
import re

path = "/Users/trevor/Desktop/ytmDownloader/illegal_music_lol"

# def load_settings():
#     with open ('settings.json') as f:
#         settings = json.load(f)
#     return settings

def load_json_opts():
    with open ('ydl_opts.json') as f:
        options = json.load(f)
    return options


def refresh_library(csv_file, path=path): # only for current files

  with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for _, dirs, file_names in os.walk(path):
      for file_name in file_names:
        print(path)
        key = mutagen.File(str(path+"/"+file_name))['TKEY'] # need something that works for mp4 and mp3
        print(key)
        bpm = mutagen.File(str(path+"/"+file_name))['TBPM']
        print(bpm)
        song = file_name.split(" - ",1)
        print(song)
        try:
          writer.writerow([song[0]]+[re.sub('.mp[0-9]','',song[1])]) 
        except IndexError:
          writer.writerow(song+["__UNKNOWN__"]+key+bpm)
    print('---Done---')
    
def seconds_to_minutes(raw_sec):
  seconds = raw_sec % 60
  min = raw_sec // 60
  return (str(min)+"min "+str(seconds)+"s")

def spotify_get_features():
    '''
    
    '''
    pass