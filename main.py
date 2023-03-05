from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import tweepy
import json
import pandas as pd
import csv
import re
from textblob import TextBlob
import string
import preprocessor as p
import os
import time

# Load credentials from json file
with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)


auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True)


def scraptweets(search_words, date_since, numTweets, numRuns):

  # Define a for-loop to generate tweets at regular intervals
  # We cannot make large API call in one go. Hence, let's try T times

  # Define a pandas dataframe to store the date:
  db_tweets = pd.DataFrame(columns = ['username', 'acctdesc', 'location', 'following',
                                      'followers', 'totaltweets', 'usercreatedts', 'tweetcreatedts',
                                      'retweetcount', 'text', 'hashtags']
                              )
  program_start = time.time()
  for i in range(0, numRuns):
    # We will time how long it takes to scrape tweets for each run:
    start_run = time.time()
    
    # Collect tweets using the Cursor object
    # .Cursor() returns an object that you can iterate or loop over to access the data collected.
    # Each item in the iterator has various attributes that you can access to get information about each tweet
    tweets = tweepy.Cursor(api.search, q=search_words, lang="ru", since=date_since,geocode="47.9173,106.9177,50km", tweet_mode='extended').items(numTweets)
  # Store these tweets into a python list
    tweet_list = [tweet for tweet in tweets]
    noTweets = 0
    for tweet in tweet_list:
    # Pull the values
      username = tweet.user.screen_name
      acctdesc = tweet.user.description
      location = tweet.user.location
      following = tweet.user.friends_count
      followers = tweet.user.followers_count
      totaltweets = tweet.user.statuses_count
      usercreatedts = tweet.user.created_at
      tweetcreatedts = tweet.created_at
      retweetcount = tweet.retweet_count
      hashtags = tweet.entities['hashtags']
      try:
        text = tweet.retweeted_status.full_text
      except AttributeError:  # Not a Retweet
        text = tweet.full_text
      # Add the 11 variables to the empty list - ith_tweet:
      ith_tweet = [username, acctdesc, location, following, followers, totaltweets,
                          usercreatedts, tweetcreatedts, retweetcount, text, hashtags]
      # Append to dataframe - db_tweets
      db_tweets.loc[len(db_tweets)] = ith_tweet
      # increase counter - noTweets  
      noTweets += 1
  # Obtain timestamp in a readable format
  to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
  # Define working path and filename
  path = os.getcwd()
  filename = path + '/data/' + to_csv_timestamp + '_byamba_tweets.csv'
  # Store dataframe in csv with creation date timestamp
  db_tweets.to_csv(filename, index = False)

  program_end = time.time()
  print('Scraping has completed!')
  print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))


  # Initialise these variables:
search_words = "*"
date_since = "2020-05-10"
numTweets = 1500
numRuns = 4
# Call the function scraptweets
scraptweets(search_words, date_since, numTweets, numRuns)

