import requests
from requests_oauthlib import OAuth1
import random

name = "Tim Lydigen"

#twitter api url's to allow for authentication
TWITTER_API_URL = 'https://api.twitter.com'
TWITTER_TIMELINE_URL = TWITTER_API_URL + '/1.1/statuses/user_timeline.json'
TWITTER_SEND_TWEET_URL = TWITTER_API_URL + '/1.1/statuses/update.json'
TWITTER_ACCOUNT_VERIFY_URL = TWITTER_API_URL + '/1.1/account/verify_credentials.json'
#declare your credentials 
def oauth1():
    auth = OAuth1('YOUR_APP_KEY', 
                  'YOUR_APP_SECRET', 
                  'USER_OAUTH_TOKEN', 
                  'USER_OAUTH_TOKEN_SECRET')
    return auth
#setting up variable for oauth authentication protocol
y = oauth1()
#setting up variable for get request
x = requests.get(TWITTER_ACCOUNT_VERIFY_URL, auth=y)
print x.status_code
#post tweet
def post_tweets(tweet):
    with open('text.txt') as f:
        #tweets a single tweet
        file = random.choice(f.readlines())
        filter(lambda tweets : len(tweets) <= 140, file)
        tweet = requests.post(TWITTER_SEND_TWEET_URL, {'status':file}, auth=y)
        print tweet.status_code
        #allows for better visibility of whats posting
        print tweet.json()
post_tweets('status')

