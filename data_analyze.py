#!/usr/bin/python3

import tweepy
from textblob import TextBlob
# definng consumer key & secret
# making connection with twitter api
c_key=""

c_sec=""

# token key & secret
# to search & get information you need to use token
t_key=""

t_sec=""

# connecting twitter APi
auth_session=tweepy.OAuthHandler(c_key,c_sec)

#print(dir(auth_session))

# setting , sending token key and secret
auth_session.set_access_token(t_key,t_sec)

# now accessing API 

api_connect=tweepy.API(auth_session)

# searching for data
topic=api_connect.search('M.S Dhoni')

for i in topic:
    # tokenized and clean data
    blob_data=TextBlob(i.text)
    # applying sentiment(analyser) output will be polarity
    print (blob_data.sentiment)
    


#print (topic)
