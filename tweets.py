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
import sqlite3



df = pd.read_csv('/Users/enkhbat/my_functions/twitter/mongol_tweets/data/enkhbat.csv')

conn = sqlite3.connect('data/tweets.db')
table_name="tweets"
df.to_sql(table_name, conn, if_exists='append', index=False)
# part.to_csv("zuvhun_tweets.csv")
print('Done')

