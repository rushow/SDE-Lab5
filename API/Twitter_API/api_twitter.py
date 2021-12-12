import os
import tweepy as tw
import pandas as pd
from datetime import datetime
import json

#consumer Key
consumer_key="Xz1Gi8qMiX0RDgbXSY33II8BB"
consumer_secret="NzCn4dSLvaJGxYZHzJyHnsyJ93KiJfM03cJhjBkjduIvRAeabG"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAO3AWgEAAAAA9xqjDcIkoan0PxrDixk6ayBO6SY%3DTd9kHDvkOxPViALPnmkgCulTMlOh69YozuGcog1GozeZVlidnG"
access_token="1468521297118478336-SFvUrKRb4394arDgqQjZUattq0Y7Ee"
access_token_secret="6BddGxqoNdH1b6y8VQCz1uWgqGvDKv9kYKCCmKNWSjkwV"

auth = tw.OAuthHandler(consumer_key, consumer_secret,)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
def search_tweet():
    trending=["#Afghanistan","#COVID","#FIFA22","#Dune","#AMC","#SquidGame","#T20worldcup","#Ethereum","#TigerWoods","#Batllefield2042"]
    final_dataset=[]
    for trends in trending:
        search_words = trends
        date_since = "2018-11-16"
        #search only tweets about search words which are the most popular but can look for recent or mixed 
        #we can look for tweets before a certain date with until
        tweets = tw.Cursor(api.search_tweets,
                    q=search_words,
                    lang="en",
                    result_type="mixed").items(100)
        data_sets=[]
        for tweet in tweets:
            #for more information look here: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets#example-response
            new_datetime = tweet.created_at.strftime('%Y-%m-%d')
            data_sets.append([tweet.id,trends,new_datetime,tweet.user.name,tweet.user.location,tweet.lang, tweet.text])
        tweet_text = pd.DataFrame(data=data_sets, 
                        columns=['id','subject',"date","user_name","location","language","text"])
        final_dataset.append(tweet_text)
    final_dataset=pd.concat(final_dataset)
    final_dataset.to_json(r'./API/Twitter_API/tweets.json',orient='records',encoding="utf-8-sig")
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
#search_tweet()
utf_correction()
