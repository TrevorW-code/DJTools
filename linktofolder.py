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

from pytube import YouTube
from pytube import Playlist
import sys
import csv

# with open('Songlist.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))

def timeToMin(raw_sec):
    seconds = raw_sec % 60
    min = raw_sec // 60
    return (str(min)+"min "+str(seconds)+"s")

if sys.argv[1] == "s":
    link = str(sys.argv[2])
    yt=YouTube(link)
    t=yt.streams.filter(only_audio=True)
    path = "/Users/trevor/Desktop/ytmDownloader/test"
    filename=yt.title+" - "+yt.author[:-8]+".mp3" # check to see if mp3 works
    print(yt.title+" - "+yt.author[:-8])
    print("length: "+timeToMin(yt.length))
    print('download to: '+path)
    t[1].download(path,filename=filename)

if sys.argv[1] == 'pl':
    link = str(sys.argv[2])
    pl = Playlist(link)
    for video in pl.videos:
        print(f'Downloading: {video.title}')
        t=video.streams.filter(only_audio=True)
        path = "/Users/trevor/Desktop/ytmDownloader/test"
        filename=video.title+" - "+video.author[:-8]+".mp3" # check to see if mp3 works
        print("Name: "+video.title+" - "+video.author[:-8])
        print("Length: "+timeToMin(video.length))
        print('Download Path: '+path)
        print('\n\n')
        t[1].download(path,filename=filename)




