#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import pandas as pd
import numpy as np
import regex as re
import os
import json
from datetime import datetime, date, time, timedelta
import time

# Load credentials from json file
with open("../twitter_credentials.json", "r") as file:
	creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True)

# Define the search term and the date_since date as variables
search_words = "ЗӨВ ХҮН"
date_since = "2017-04-25"
date_to="2020-05-15"

def get_tweets_csv(search_words, date_since):
	new_search = search_words + " -filter:retweets"

	tweets = tweepy.Cursor(api.search, 
	                           q=search_words,
	                           lang="ru",
                             geocode="47.9173,106.9177,20km",
                             since=date_since,
														 tweet_mode='extended').items(500)

	users_locs = [[tweet.id_str, tweet.user.screen_name, tweet.full_text, tweet.created_at, tweet.user.location
	              ,tweet.favorite_count,tweet.retweet_count] for tweet in tweets]
	users_locs

	tweet_text = pd.DataFrame(data=users_locs, 
	                    columns=["id", "user", "tweets","date","location","favorites","retweets"])

	return tweet_text

df=get_tweets_csv(search_words, date_since)
reduc=df.drop_duplicates(subset=['tweets'])
part=reduc.sort_values(by=['retweets'], ascending=False)
part=part[['tweets','retweets']]
# part=part[part.retweets>10]

# def get_user_name(x):
# 	domain= x.split('@')[1]
# 	name=domain.split(':')[0]
# 	return name


# part["maker"]=part.tweets.map(lambda x: get_user_name(x))
# df.to_csv("zuvhun.csv", index=False)
conn = sqlite3.connect('data/tweets.db')
table_name="tweets"
df.to_sql(table_name, conn, if_exists='append', index=False)
# part.to_csv("zuvhun_tweets.csv")

