# Arnnop Hualchareonthon (ah3200)
#Import the necessary methods from tweepy library
import tweepy
import sys
import json

#Access Token and Access Token Secret of Twitter API (apps)
access_token = ""
access_token_secret = ""

if __name__ == '__main__':

#   To run program: python twitterdownload.py CONSUMER_KEY CONSUMER_SECRET
    consumer_key = sys.argv[1]
    consumer_secret = sys.argv[2]
    
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = api.home_timeline()

    with open('twitterdata.csv','w') as f:
        for tweet in public_tweets:
            print str(tweet.id_str) + str(tweet.created_at) + tweet.text
            f.write(str(tweet.id_str) + ',' + str(tweet.created_at) + ',' + tweet.text.encode("utf-8") + '\n')
    f.closed

    
