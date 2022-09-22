import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "u88LUzIHUXUrMV1yGTDKLs1oe"
access_secret = "8VSf84NVbtj7L1UQ399Faal3vveq7tKwbgusHeRSGAZ8UDpsP2"
consumer_key = "1070169780-bzC64vQOP6LKFGXECbTNZB8vNfZ4O3XcN3nCCeC"
consumer_secret = "7TStZjgthxGDviEho6UbidXit4DHIuq5xu2n47NTjI8z0"

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
tweet_list = []
for tweet in tweets:
    text = tweet._json["full_text"]

    refined_tweet = {"user": tweet.user.screen_name,
                     'text': text,
                     'favorite_count': tweet.favorite_count,
                     'retweet_count': tweet.retweet_count,
                     'created_at': tweet.created_at}

    tweet_list.append(refined_tweet)
df = pd.DataFrame(tweet_list)
df.to_csv("elonmusk_twitter_data.csv")
