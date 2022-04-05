from pytube import YouTube
import re
import sys

file = str(sys.argv[1])
# correct_link = re.sub("music.","",file)
yt=YouTube(file)
t=yt.streams.filter(only_audio=True)
path = "/Users/trevor/Desktop/ytmDownloader/test"
t[1].download(path)
