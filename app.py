
import textblob
import tweepy
import os
import json

consumer_key = os.environ.get('twitter_consumer_key')
consumer_secret = os.environ.get('twitter_consumer_secret')
access_token = os.environ.get('twitter_access_token')
access_token_secret = os.environ.get('twitter_access_token_secret')
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweetSearch(phrase='bitcoin'):
    public_tweets = api.search(phrase, result_type='recent', count=100)
    tweetlist = []
    for tweet in public_tweets:
        analysis = textblob.TextBlob(tweet.text)
        tweetlist.append(json.dumps(tweet._json))
    return tweetlist

def getStatus():
    status = api.rate_limit_status()
    print('Resources: ')
    resources = status.get('resources')
    for category in resources:
        print('----', category)
        for resource in resources.get(category):
            print("    ----{} : Remaining: {}, Limit; {}".format(resource, resources.get(category).get(resource).get('remaining'), resources.get(category).get(resource).get('limit')))
    return status

if __name__ == '__main__':
    tweety = tweetSearch()
    for tweet in tweety: print(tweet)
    getStatus()