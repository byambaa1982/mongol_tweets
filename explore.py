import pandas as pd

df=pd.read_csv("data/20200515_183816_byamba_tweets.csv")

#------------ What tweeets go viral today
rt=df.drop_duplicates(subset=['text'])
rt=df.sort_values(by=['retweetcount'], ascending=False)


#-----------Who has the most followers-----

follower=df.drop_duplicates(subset='username')
fl=follower.sort_values(by=['followers'], ascending=False)
fl=fl[['username', 'following', 'followers', 'totaltweets']]
fl.to_csv('sorted_by_follwers.csv')

#-----------Who tweets most-----

tws=df.drop_duplicates(subset='username')
tws=tws.sort_values(by=['totaltweets'], ascending=False)
tws=tws[['username', 'following', 'followers', 'totaltweets']]
tws.to_csv("sorted_by_tweets.csv", index=False)