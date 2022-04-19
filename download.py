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


# looked for a way to set file properties in python, 

from fileinput import filename
from tabnanny import check
from pytube import YouTube, Playlist
import pdb
import os
import logging
import pandas as pd
import sys
import csv
import re
import pprint

from utils import refresh_library, seconds_to_minutes, path


class Video:
  def __init__(self, title, author):
    self.title = title
    self.author = author

def yt_stats(obj,filename=filename):
    print('\n')
    print("Name: "+filename)
    print("Length: "+seconds_to_minutes(obj.length))
    print("Listens: "+str(obj.views))
    print('Download Path: '+path)

def clean_input(string):
  '''
  clean input with a variety of methods
  '''
  bad_characters = '/\\,.!@#$%^&*(){}`~'
  for bad_character in bad_characters:
    for letter in string:
      if letter == bad_character:
        re.sub(bad_character, '', string)
  return string

def add_song_data(csv_file,song):

  '''
  adds song to csv as it is downloaded
  '''
  pass

  # with open(csv_file, 'a', newline='') as csvfile: # change to append to check for songs
  #     writer = csv.writer(csvfile, delimiter=',')
  #     writer.writerow([song.title]+[song.author[:-8]])

def download_song(link):
  '''
  use mutagen for song metadata
  '''
  # yt=YouTube(link)
  # t=yt.streams.filter(only_audio=True) 
  # check_song('Songlist.csv',yt.title,yt.author) # bounce when this happens
  # filename=yt.title+" - "+yt.author[:-8]+".mp4"  # AS: why is this only the last 8 chars?
  # # AS: titles that have slashes in them or other naughty characters will break this ... probably use
  # # a built-in method to make these safe
  # filename = re.sub("\"","\xe2",filename)
  # yt_stats(yt,filename=filename)
  # t[1].download(path,filename=filename)
  # print('---Sucess---')
  # print('\n')

  yt=YouTube(link)
  t=yt.streams.filter(only_audio=True)
  checkSong('Songlist.csv',yt.title,yt.author)
  filename=yt.title+" - "+yt.author[:-8]+".mp4"
  filename = re.sub("\"","\xe2",filename)

  print('\n')
  print("Name: "+filename)
  print("Length: "+seconds_to_minutes(yt.length))
  print("Listens: "+str(yt.views))
  print('Download Path: '+path)
  t[1].download(path,filename=filename)
  print('---Sucess---')
  print('\n')


def download_playlist(link):
  # AS: does the yt library have a download playlist feature?? seems like core functionality imo
  # AS: also you could maybe parallelize this if you're feeling ~spicy~
  # TW: I am feeling ~spicy~
  
  pl = Playlist(link)
  for idx, video in enumerate(pl.videos):
    
    print(f"[{idx+1}/{len(pl)}]")  # AS: nice :)

    vid_list.append(Video(video.title,video.author)) # maybe delete this

    print(f'Downloading: {video.title}')
    song_stream=video.streams.filter(only_audio=True)

    filename=video.title+" - "+video.author[:-8]+".mp4"
    filename = re.sub("\"","’",filename) # do different 

    yt_stats(video,filename=filename)
    # song_stream[1].download(path,filename=filename) # issue with this sometimes
    
    print('---Sucess---')
    print('\n')

"""
AS: I think this should be wrapped in if __name__ == '__main__' ... could be totally wrong ngl
TW: yeah the question is how do I start a session, I was thinking of maube using while True: and then have it wrap to an input if that makes sense

mmh yeah like just let the user input whatever they like and the system would stay running?
TW:yes, because I hate typing in python download.py everytime

TW: also having a way to distinguish when you are downloading during an actual party or not by activating "session"
TW: making the recommender soon for this, just need to finish the objects

oh yea

i'd clean this up a bit before the recommender stuff tbh

TW: yes, this is what I am thinking, I agree
"""

if sys.argv[1] == 's':
  link = str(sys.argv[2])
  download_song(link)

if sys.argv[1] == 'pl':
  vid_list = []
  link = str(sys.argv[2])
  download_playlist(link)
  add_song_data("Songlist.csv", vid_list)

if sys.argv[1] == 'refresh':
  refresh_library("Songlist.csv")

if sys.argv[1] == 'test':
  pdb.set_trace
  clean_input()