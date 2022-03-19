import tweepy
import time
from credentials import api


users = tweepy.Cursor(api.followers, screen_name="BBnours_").items()


while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        time.sleep(1)
        user = next(users)
    except StopIteration:
        break
    print("@" + user.screen_name)
