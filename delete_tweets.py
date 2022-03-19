import tweepy
import time
import random
import os 
from credentials import api

for status in tweepy.Cursor(api.user_timeline).items():
    try:
        api.destroy_status(status.id)
        print("Deleted:", status.id)
    except:
        print("Failed to delete:", status.id)
