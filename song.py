from youtube_search import YoutubeSearch
import os
from pytube import YouTube

def dl(song):
    for i in song:
        base = "https://www.youtube.com"
        result = YoutubeSearch(i, max_results=1).to_dict()
        suffix = result[0]['url_suffix']
        link = base + suffix
        out_file = YouTube(link).streams.filter(only_audio=True).first().download(os.getcwd())
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Download Completed: "+i)

