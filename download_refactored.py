import sys
from yt_dlp import YoutubeDL

ydl_opts = {'format': 'bestaudio'}
with YoutubeDL(ydl_opts) as ydl:
    ydl.download([sys.argv[1]])