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

from pytube import YouTube
from pytube import Playlist
import sys
import csv

path = "/Users/trevor/Desktop/illegal_music_lol/disco"

def timeToMin(raw_sec):
    seconds = raw_sec % 60
    min = raw_sec // 60
    return (str(min)+"min "+str(seconds)+"s")

class Video:
  def __init__(self, title, author):
    self.title = title
    self.author = author

# Check downloads if they are there
# def checkDownloads(csv, list): # fix this
#     with open(csv, newline='') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             print(list[row].title, list[row].author)

def updateDownloads(csv_file,listy):
    with open(csv_file, 'w', newline='') as csvfile: # change to append to check for songs
        writer = csv.writer(csvfile, delimiter=',')
        for video in listy:
            writer.writerow([video.title]+[video.author[:-8]])

def download_song(link):
    yt=YouTube(link)
    t=yt.streams.filter(only_audio=True)
    # path = "/Users/trevor/Desktop/ytmDownloader/test
    filename=yt.title+" - "+yt.author[:-8]+".mp4"
    print(yt.title+" - "+yt.author[:-8])
    print("length: "+timeToMin(yt.length))
    print('download to: '+path)
    t[1].download(path,filename=filename)

def download_playlist(link):
  pl = Playlist(link)
  for video in pl.videos:
      filename=video.title+" - "+video.author[:-8]+".mp3"
      vid_list.append(Video(video.title,video.author))
      print(f'Downloading: {video.title}')
      t=video.streams.filter(only_audio=True)
      # path = "/Users/trevor/Desktop/ytmDownloader/test"
      filename=video.title+" - "+video.author[:-8]+".mp4" 
      print("Name: "+video.title+" - "+video.author[:-8])
      print("Length: "+timeToMin(video.length))
      print('Download Path: '+path)
      print('\n')
      t[1].download(path,filename=filename) # issue with this sometimes

if sys.argv[1] == "s":
    link = str(sys.argv[2])
    download_song(link)

if sys.argv[1] == 'pl':
    vid_list = []
    link = str(sys.argv[2])
    download_playlist(link)
    updateDownloads("Songlist.csv",vid_list)