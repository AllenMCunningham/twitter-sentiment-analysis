

import twitter_connection as twitter

if __name__ == '__main__':
    tweetlist = twitter.tweetSearch()
    for tweet in tweetlist: print(tweet)
    twitter.getStatus()