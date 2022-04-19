import sys
from utils import load_json_opts
from yt_dlp import YoutubeDL


ydl_opts = load_json_opts()

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([sys.argv[1]])