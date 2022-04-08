'''

want to add flags for downloading playlists (pl or p) and individual songs (s)

def handle_one():
  do_stuff

def handle_two():
  do_stuff

def handle_three():
  do_stuff


{'one': handle_one, 
 'two': handle_two, 
 'three': handle_three}[option]()

'''

# check csv for song id stuff
# if not in csv, add to csv
# remember to activate environment (DS) locally
# make a way to change path on the fly?
# error in downloading playlist causes not to update csv
# make a way to create a new folder on the fly as well

# from typing_extensions import Self
from pytube import YouTube
from pytube import Playlist
import os
import argparse
import pandas as pd
import sys
import csv
import re

path = "/Users/trevor/Desktop/ytmDownloader/illegal_music_lol/temp"

def timeToMin(raw_sec):
  seconds = raw_sec % 60
  min = raw_sec // 60
  return (str(min)+"min "+str(seconds)+"s")

class Song(YouTube):
  def __init__(self, url):
    self.filename = self.title+" - "+self.author[:-8]+".mp4" # is this how inheritance works?
    super().__init__(url) # how do I inherit from this? do I need every single thing


  def song_stats(instance):
    # time, grab song data from spotify api or tunebat
    print("Name: "+instance.title+" - "+instance.author[:-8])
    print("Length: "+timeToMin(instance.length))
    print("Listens: "+str(instance.views))
    print('Download Path: '+path)
    print('success')
    # https://developer.spotify.com/documentation/web-api/reference/#/operations/get-several-audio-features
    # https://medium.com/swlh/spotify-song-prediction-and-recommendation-system-b3bbc71398ad

  def download_song(instance,filename):
    pass
    t=instance.streams.filter(only_audio=True)
    print('download test')
    # t[1].download(path,filename=filename)


#     yt=YouTube(link)
#     t=yt.streams.filter(only_audio=True)
#     checkSong('Songlist.csv',yt.title,yt.author)
#     filename=yt.title+" - "+yt.author[:-8]+".mp4"
#     filename = re.sub("\"","’",filename) # do different 



#     print('---Sucess---')



# if sys.argv[1] == 's':
#     link = str(sys.argv[2])
#     yt=YouTube(link)
#     song = Song(yt)
#     # song.song_stats


# if sys.argv[1] == 'pl':
#     vid_list = []
#     link = str(sys.argv[2])
#     download_playlist(link)
#     updateDownloads("Songlist.csv",vid_list)
















class Video:
  def __init__(self, title, author):
    self.title = title
    self.author = author


def scanFiles(csvFile,path=path):
  '''
  I need a function that scans every mp4 file and puts it into the csv without reading into anything --> write to file?
  '''
  # for _, dirs, file in os.walk(path):
    # if file
    # if the format is "Arist - Song"
      # split on Artist - Song
    # if it is not in "Arist - Song"
      # first column is song, second is unknown
# Check downloads if they are there --> What is a better structure? maybe add to list in check song, interesting idea

def checkSong(csv_file, song, artist): # fix this
  '''
  still trying to figure out when I should do the checks for the song. 
  I should do it before I download the song, and maybe this function has the download in it?
  '''
  pass
#     with open(csv_file, 'rt') as f:
#       reader = csv.reader(f, delimiter=',')
#       for row in reader: # make it so that it checks every row, not just the first row
#             print(row)
#             if (song == row[0]) and (artist == row[1]): # test song
#                 print('False')
#                 return False
#             else:
#                 print('True')
#                 return True

def updateDownloads(csv_file,song):
  pass
  # with open(csv_file, 'a', newline='') as csvfile: # change to append to check for songs
  #     writer = csv.writer(csvfile, delimiter=',')
  #     writer.writerow([song.title]+[song.author[:-8]])

def download_song(link):
    yt=YouTube(link)
    t=yt.streams.filter(only_audio=True)
    checkSong('Songlist.csv',yt.title,yt.author)
    filename=yt.title+" - "+yt.author[:-8]+".mp4"
    filename = re.sub("\"","’",filename) # do different 

    print('\n')
    print("Name: "+filename)
    print("Length: "+timeToMin(yt.length))
    print("Listens: "+str(yt.views))
    print('Download Path: '+path)
    t[1].download(path,filename=filename)
    print('---Sucess---')
    print('\n')

def download_playlist(link):
  pl = Playlist(link)
  for idx,video in enumerate(pl.videos):
    print(f"[{idx+1}/{len(pl)}]")
    # if checkSong('Songlist.csv',video.title,video.author[:-8]):
    vid_list.append(Video(video.title,video.author)) 
    print(f'Downloading: {video.title}')
    t=video.streams.filter(only_audio=True)
    filename=video.title+" - "+video.author[:-8]+".mp4"
    filename = re.sub("\"","’",filename) # do different 
    print("Name: "+video.title+" - "+video.author[:-8])
    print("Length: "+timeToMin(video.length))
    print("Listens: "+str(video.views))
    print('Download Path: '+path)
    t[1].download(path,filename=filename) # issue with this sometimes
    print('---Sucess---')
    print('\n')

if sys.argv[1] == 's':
    link = str(sys.argv[2])
    download_song(link)

if sys.argv[1] == 'pl':
    vid_list = []
    link = str(sys.argv[2])
    download_playlist(link)
    updateDownloads("Songlist.csv",vid_list)