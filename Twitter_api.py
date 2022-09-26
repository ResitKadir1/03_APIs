import Credentials
import tweepy
import pandas as pd
import os

if not os.path.exists("Twitter_API_data"):
    os.makedirs("Twitter_API_data")
Twitter_API_data = "Twitter_API_data/"

# ADD VALUES HERE
api_key = Credentials.api_key
secret =  Credentials.secret
#bearer_token = ''
access_token = Credentials.access_token
access_token_secret = Credentials.access_token_secret

#### v1.1 with Tweepy

# OAuth authentication
auth = tweepy.OAuth1UserHandler(api_key, secret, access_token, access_token_secret)
api = tweepy.API(auth)

#################################################

# get tweets from own timeline
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
####################################################


# streaming with API v1.1 (soon to be deprecated)
class MyStream(tweepy.Stream):
    """
    Extend the tweepy.Stream API to do something with the tweets received
    """
    def on_status(self, status):
        print(status.text)

# get all tweets containing a given keyword
#given_words = "amedspor"
stream = MyStream(api_key, secret, access_token, access_token_secret)
given_words_=stream.filter(track=['amedspor'])
given_words_.to_csv(Twitter_API_data+"Twitter_API_data.csv", encoding='utf-8', index=False)
print(given_words_)




