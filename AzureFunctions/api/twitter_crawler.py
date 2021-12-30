import os
import tweepy as tw
import pandas as pd
from datetime import datetime
import json
import access

#consumer Key
consumer_key= 'DSn8jLXd22z5LuBB1TEYhwRiL'
consumer_secret= 'h0E4JCRuEKXgxbmsR8kseEa7Rapf5ldmFW57pIhJCafBVLwlO4'
access_token= '1468521297118478336-j0GJhq6cWkh3ZqG4S1fGgbzlshyTNm'
access_token_secret= 'nNwbXu4x9xNjiv0H4VHc4sRQZIMFidIJZlJMFXmdJVLfx'

BEARER_TOKEN= 'AAAAAAAAAAAAAAAAAAAAAO3AWgEAAAAASqsiTbO%2BGujU%2FaS75GqyYI7wumM%3DyMDELmKTTXXcLfzrcKfUMYF2AHdiVfSV4jLjDJDjM90O4nd49L'

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/


def search_tweet(trends):

    if trends is None:
        trends=["#Afghanistan","#COVID","#FIFA22","#Dune","#AMC","#SquidGame","#T20worldcup","#Ethereum","#TigerWoods","#Batllefield2042"]
    else:
        trends = trends.split(',')

    rows = []
    for trend in trends:
        #search only tweets about search words which are the most popular but can look for recent or mixed 
        #we can look for tweets before a certain date with until
        tweets = tw.Cursor(api.search_tweets,
                    q=trend,
                    lang="en",
                    result_type="mixed").items(10)

        for tweet in tweets:
            #for more information look here: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets#example-response
            row = {
                'id': tweet.id,
                'subject': trend,
                'date': tweet.created_at.strftime('%Y-%m-%d'),
                'user_name': tweet.user.name,
                'location': tweet.user.location,
                'language': tweet.lang,
                'text': tweet.text,
            }
            rows.append(row)
   
    return rows

def utf_correction():
    tweets=[]
    with open("./API/Twitter_API/tweets.json") as jsonFile:
        for jsonObj in jsonFile:
            tweet = json.loads(jsonObj)
            tweets.append(tweet)
        jsonFile.close()
    with open("./API/Twitter_API/tweets_corect.json","w",encoding='utf-8') as jsonFile:
        for tweet in tweets:
            for text in tweet:
                    text["text"]=text["text"].strip('\n\n')
                    text["text"]=text["text"].replace('\n',' ')
                    text["location"]=text["location"].strip()
            json.dump(tweet,jsonFile,ensure_ascii=False)

# search_tweet()
#utf_correction()
