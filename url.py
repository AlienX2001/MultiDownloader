import os
from pytube import YouTube

def dl(url):
    for i in url:
        YouTube(i).streams.filter().first().download(os.getcwd())
        print("Download Completed: "+i)
