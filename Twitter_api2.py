import requests
import tweepy

"""
#### v2 with Requests
Version 2 of the Twitter API has an updated set of endpoints and more functionalities.
 If you can get an API key in the Academic Research track, it allows you to search for tweets posted
 at any point in the past (no other method allows you to do that).
 It is more volume-restricted than v1.1 though.
 The standard track is limited to 0.5M tweets per month, the Elevated track to 2M per month,
and the Academic Research track is limited to 10M per month.

"""

# API v2 endpoint for recent tweets search
endpoint_url = 'https://api.twitter.com/2/tweets/search/recent'

# authentication-->
headers = {'Authorization': f'Bearer {bearer_token}'}

# API v2 allows you to specify the fields to be returned
tweet_fields = ['author_id', 'created_at', 'id', 'text', 'withheld']
tweet_fields = ','.join(tweet_fields)
user_fields = ['created_at', 'description', 'id', 'location', 'name', 'username']
user_fields = ','.join(user_fields)

query = 'ukraine'
query_params = {'query': query,
                'tweet.fields': tweet_fields,
                'user.fields' : user_fields,
                'max_results': 10,
               }
response = requests.request('GET', endpoint_url, headers=headers, params=query_params)
response.json()['data']



###### v2 with Tweepy####

class MyStreamV2(tweepy.StreamingClient):
    def on_data(self, data):
        print(data)

stream = MyStreamV2(bearer_token)
stream.sample()
