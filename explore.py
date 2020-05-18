import pandas as pd
import json
import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
from collections import Counter
import sys
# Load credentials from json file
with open("../twitter_credentials.json", "r") as file:
    creds = json.load(file)

auth = tweepy.OAuthHandler(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])
auth.set_access_token(creds['ACCESS_TOKEN'], creds['ACCESS_SECRET'])
api = tweepy.API(auth, wait_on_rate_limit=True)
# df=pd.read_csv("data/20200515_183816_byamba_tweets.csv")

# #------------ What tweeets go viral today
# rt=df.drop_duplicates(subset=['text'])
# rt=df.sort_values(by=['retweetcount'], ascending=False)


# #-----------Who has the most followers-----

# follower=df.drop_duplicates(subset='username')
# fl=follower.sort_values(by=['followers'], ascending=False)
# fl=fl[['username', 'following', 'followers', 'totaltweets']]
# fl.to_csv('sorted_by_follwers.csv')

# #-----------Who tweets most-----

# tws=df.drop_duplicates(subset='username')
# tws=tws.sort_values(by=['totaltweets'], ascending=False)
# tws=tws[['username', 'following', 'followers', 'totaltweets']]
# tws.to_csv("sorted_by_tweets.csv", index=False)

df=pd.read_csv('canditates.csv')
account_list=list(df.screen_name)
def desc_users():
	users={}
	users["name"]=[]
	users["screen_name"]=[]
	users["description"]=[]
	users["statuses_count"]=[]
	users["friends_count"]=[]
	users["followers_count"]=[]
	users["account_age"]=[]
	users["average_tweets_per_day"]=[]
	if len(account_list) > 0:
		for target in account_list:
			try:
				item = api.get_user(target)
				users["name"].append(item.name)
				users["screen_name"].append(item.screen_name)
				users["description"].append(item.description)
				users["statuses_count"].append(item.statuses_count)
				users["friends_count"].append(item.friends_count)
				users["followers_count"].append(item.followers_count)
				tweets = item.statuses_count
				account_created_date = item.created_at
				delta = datetime.utcnow() - account_created_date
				account_age_days = delta.days
				users["account_age"].append(account_age_days)
				print("Account age (in days): " + str(account_age_days))
				if account_age_days > 0:
					print("Average tweets per day: " + "%.2f"%(float(tweets)/float(account_age_days)))
					users["average_tweets_per_day"].append(float(tweets)/float(account_age_days))
			except:
				print("not found:{}".format(target))
	df=pd.DataFrame(users, columns=users.keys())
	return df.to_csv("can_stats.csv", index=False)

desc_users()
tws=pd.read_csv("can_stats.csv")
tws=tws.sort_values(by=['average_tweets_per_day'], ascending=False)
tws=tws[['name', 'average_tweets_per_day']]
tws=tws.round(2)
tws.to_csv("cand_sorted_by_tweets.csv", index=False)

