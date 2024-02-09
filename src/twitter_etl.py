import tweepy
import pandas as pd
import json
from datetime import datetime
import s3fs

def run_twitter_etl():
    access_key = "1143309226305105920-OTpCCUuPIBOIiSXgpcGYxsS8SJMHIN"
    access_secret = "dUTfz3JbJiq0ZqIzzhKddrO1BN2ogtun9RK6x9xYfFLlj"
    consumer_key = "O5Adm6r3TI2G9CfNO2R3JSIbK"
    consumer_secret = "b2PWvCBeW7KH7dLVGE8wwPa2GJ5chomsEMEboXhbtw06TfjOKV"
    csv_name = "lorenzo_twitter_data.csv"
    bucket_location = ""

    #Twitter Auth
    auth = tweepy.OAuth1UserHandler(
        consumer_key, consumer_secret,
        access_key, access_secret
    )

    # Creating API Auth
    api = tweepy.API(auth)

    tweets = api.user_timeline(screen_name='@Lorenzouriel6',
                            # 200 is the maximum allowed count
                            count=200,
                            include_rts = False,
                            # Necessary to keep full text
                            tweet_mode = 'extended'   
                            )

    print(tweets)

    tweet_list = []
    for tweet in tweets:
        text = tweet._json["full_text"]

        refined_tweet = {"user": tweet.user.screen_name,
                        'text': text,
                        'favortite_count': tweet.favortite_count,
                        'retweet_count': tweet.retweet_count,
                        'created_at': tweet.created_at}
            
        tweet_list.append(refined_tweet)

    df = pd.DataFrame(tweet_list)
    df.to_csv(bucket_location + csv_name)