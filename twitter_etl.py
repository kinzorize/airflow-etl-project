import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = ""
access_secret = ""
consumer_key = ""
consumer_secret = ""

# Twitter authentication
auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# Create an API object
api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count=200,  # maximum count of 200
                           include_rts=False,
                           tweet_mode='extended'  # Necessary to keep full text
                           )
print(tweets)
