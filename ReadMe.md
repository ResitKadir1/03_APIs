## Marvel API


Create and account on https://developer.marvel.com/. In the section "Get a Key", you can generate a new public/privare key pair. 

Go to https://developer.marvel.com/docs to see the full specification of API calls



#### Marvel API python wrapper
Many API have "wrappers" available in several languages. Wrappers are just pieces of code that manage the http requests and handle the responses (what we did in the code above), so that you can call simple
methods to get results directly.



# Reddit API
#### OAuth authentication
Got to https://www.reddit.com/prefs/apps and create a new application


## Pushshift

Pushift is a service that collects social media data using APIs. It stores data in third-party servers. You can query the pushift API to get Reddit data (no auth required). PMAW is a python wrapper for the Pushift API. 

Pushift API: https://github.com/pushshift/api

PMAW: https://github.com/mattpodolak/pmaw


# Twitter API

Go to https://developer.twitter.com/en/apply-for-access and apply for access

Then go to https://developer.twitter.com/en/portal/projects-and-apps, create a project and get the API credentials

API v1.1 docs: https://developer.twitter.com/en/docs/twitter-api/v1

API v2 docs: https://developer.twitter.com/en/docs/twitter-api/early-access

Twitter API rate limits (v2): https://developer.twitter.com/en/docs/twitter-api/rate-limits

Twitter API rate limits (v1.1): https://developer.twitter.com/en/docs/twitter-api/v1/rate-limits

Step-by-step guide for beginners: https://developer.twitter.com/en/docs/tutorials/step-by-step-guide-to-making-your-first-request-to-the-twitter-api-v2