import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    """
    Extracts data from Twitter, transforms it, and loads it into a CSV file stored in an S3 bucket.

    Returns:
        None

    Raises:
        None

    """
    access_key = ["YOUR ACCESS TOKEN"]
    access_secret = ["YOUR ACCESS SECRET"]
    consumer_key = ["YOUR API KEY"]
    consumer_secret = ["YOUR API SECRET"]
    csv_name = "lorenzo_twitter_data.csv"  #["YOU CSV FILE NAME"]
    bucket_location = "s3://lorenzo-airflow-twitter-etl/"  #["YOUR S3 BUCKET"]

    # Twitter Auth
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_key, access_secret
    )

    # Creating API Auth
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@Lorenzouriel6',
                               # 200 is the maximum allowed count
                               count=200,
                               include_rts=False,
                               # Necessary to keep full text
                               tweet_mode='extended'
                               )
    
    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                         'text': text,
                         'favortite_count': tweet.favorite_count,  # Corrected typo: 'favorite_count'
                         'retweet_count': tweet.retweet_count,
                         'created_at': tweet.created_at}

        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv(bucket_location + csv_name)