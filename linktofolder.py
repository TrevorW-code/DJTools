'''
want to add flags for downloading playlists (pl or p) and individual songs (s)

why does it download double the time?


'''

from pytube import YouTube
import sys
import re

def timeToMin(raw_sec):
    seconds = raw_sec % 60
    min = raw_sec // 60
    return (str(min)+"min "+str(seconds)+"s")

link = str(sys.argv[1])
yt=YouTube(link)
t=yt.streams.filter(only_audio=True)
path = "/Users/trevor/Desktop/ytmDownloader/test"
filename=yt.title+" - "+yt.author[:-8]+".mp3" # check to see if mp3 works
print(yt.title+" - "+yt.author[:-8])
print("length: "+timeToMin(yt.length))

print('download to: '+path)
t[1].download(path,filename=filename)

path_to_download = path+"/"+re.sub(" ","\\ ",filename)
print(path_to_download)

# .order_by('resolution')
# scoped in the right place?





