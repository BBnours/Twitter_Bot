# Anime Wallpaper Bot
import tweepy
import time
import random
import os
from credentials import api

# parcour de dossier et post

os.chdir('C:/Users/olivier/Pictures/wallpaperAnime')
files = os.listdir('.')
for anime_image in os.listdir('.'):
    index = random.randrange(0, len(files))
    text ='Desktop Wallpaper #Anime #Wallpaper #AnimeWallpaper'
    api.update_with_media(files[index], status=text)
    time.sleep(600)




