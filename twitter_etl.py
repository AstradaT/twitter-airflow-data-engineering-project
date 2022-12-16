import tweepy
import pandas as pd 
import json
from datetime import datetime
import s3fs 

def run_twitter_etl():

    access_key = "KSxoWEQzPGbDwsdONq9kmAOsP" 
    access_secret = "6jn7zvTmDAvWHEpHMi50jo8XEX7zPScWpBBv2xRLKsnx80y1bd" 
    consumer_key = "1357174219-HOPhTQVgtfOThqOfWDN5fcvTSnzg0PbisZRbtaQ"
    consumer_secret = "tZjKx72Yih9RJNFZnZhrbEHHqhNqkMsE2yHmJ9nbXzAHQ"

    client = tweepy.Client("AAAAAAAAAAAAAAAAAAAAABLjkQEAAAAASmpjIBU04loRl22Rrb2fgoVViQQ%3Dx4qqvhMXqEwEryBHCGlCJpbrfivRLXYFbWiJA8VF0wz3WrGKui")
    """
    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    """
    tweets = client.get_users_tweets(id=client.get_user(username='TomiAstrada').data.id, 
                            # 200 is the maximum allowed count
                            max_results=10
                            )
    
    list = []
    for tweet in tweets.data:
        list.append([tweet.id, tweet.text])

    df = pd.DataFrame(list)
    df.to_csv('refined_tweets.csv', header=['id', 'text'])


run_twitter_etl()