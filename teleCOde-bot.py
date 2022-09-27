import os,requests,sys,time
from pytube import YouTube
from pathlib import Path


class color:
   PURPLE = '\033[95m'
   GREEN = '\033[92m'
   BOLD = '\033[1m'
   CWHITE  = '\33[37m'
   


# url = "https://api.telegram.org/bot5509518853:AAHYiazTSZH-5n5nuFJrwMXOv87Qw2fMpWQ/getUpdates"

def download_YT_Videos():
    # import os
    # from pathlib import Path

    # from pytube import YouTube
   
    link = input("Paste Your link sir: ")
    try:
        url = YouTube(link)
        print("downloading....")
        video = url.streams.get_highest_resolution()
        path_to_downloads = str(os.path.join(Path.home(), "Downloads\ytmusic"))
        video.download(path_to_downloads)
    except:
        print("error")

# //////////////// READ DATA \\\\\\\\\\\\\\\\\\

def read_Data():    
    # from all_funcs.helloprinter import *
    import requests

    url = "https://api.telegram.org/bot5509518853:AAHYiazTSZH-5n5nuFJrwMXOv87Qw2fMpWQ/getUpdates"
    parameters = {
        "offset": "175621460",
        "limit" : "20"
    }

    respon = requests.get(url , data = parameters)
    ttxt = respon.json()
    global chat
    for data in ttxt ["result"]:
        chat = data["message"] ["text"]
    print(respon)
    print(color.GREEN + "test1 completed" + color.CWHITE)

# ///////////////////////// SEND MSGS \\\\\\\\\\\\\\\\\\\\\ 


# from readData import chatter 
# import os,time
def send_Msg():
    
    # import requests 

    url = "https://api.telegram.org/bot5509518853:AAHYiazTSZH-5n5nuFJrwMXOv87Qw2fMpWQ/sendMessage"
    parameters = {
        "chat_id": "1423043294",
        "text" : chat
    }

    respon = requests.get(url , data = parameters) 
    print("text sent")
    print(chat)
    print(color.GREEN + "test2 completed" + color.CWHITE)


# \\\\\\\\\\\\\\\\\\\\\\\\ SEND PHOTOS \\\\\\\\\\\\\\\\\\\\\\\\\\\

def send_Photo():
    # import requests

    url = "https://api.telegram.org/bot5509518853:AAHYiazTSZH-5n5nuFJrwMXOv87Qw2fMpWQ/sendPhoto"
    parameters = {
        "chat_id": "1423043294",
        "photo" : "https://media.giphy.com/media/z2rAxByf9eIA6Llfhy/giphy.gif"
        # "photo" : "https://source.unsplash.com/1600x900/?nature,water"
    }

    respon = requests.get(url , data = parameters)
    print("image sent")
    print(color.GREEN + "test3 completed" + color.CWHITE)


# ------------------------------------- SEND VIDEOS --------------------------------

def send_Video():

    # import requests
    vid = "https://media.giphy.com/media/z2rAxByf9eIA6Llfhy/giphy.gif"
    url = "https://api.telegram.org/bot5509518853:AAHYiazTSZH-5n5nuFJrwMXOv87Qw2fMpWQ/sendVideo"
    parameters = {
        "chat_id": "1423043294",
        "video" : vid
    }

    respon = requests.get(url , data = parameters)
    print("video sent")
    print(color.GREEN + "test4 completed" + color.CWHITE)


# 1]read_Data
# 2]send_Msg
# 3]send_Photo
# 4]send_Video

read_Data()
send_Msg()
send_Photo()
send_Video()






print("thanks for using :) ")
print("")
