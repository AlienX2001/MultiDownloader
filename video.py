from youtube_search import YoutubeSearch
import os
from pytube import YouTube

def dl(video):
    for i in video:
        base = "https://www.youtube.com"
        result = YoutubeSearch(i, max_results=1).to_dict()
        suffix = result[0]['url_suffix']
        link = base + suffix
        YouTube(link).streams.filter().first().download(os.getcwd())
        print("Download Completed: "+i)