import os
import tweepy as tw
import pandas as pd
from datetime import datetime

#consumer Key
consumer_key="Xz1Gi8qMiX0RDgbXSY33II8BB"
consumer_secret="NzCn4dSLvaJGxYZHzJyHnsyJ93KiJfM03cJhjBkjduIvRAeabG"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAAO3AWgEAAAAA9xqjDcIkoan0PxrDixk6ayBO6SY%3DTd9kHDvkOxPViALPnmkgCulTMlOh69YozuGcog1GozeZVlidnG"
access_token="1468521297118478336-SFvUrKRb4394arDgqQjZUattq0Y7Ee"
access_token_secret="6BddGxqoNdH1b6y8VQCz1uWgqGvDKv9kYKCCmKNWSjkwV"

auth = tw.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
#https://www.earthdatascience.org/courses/use-data-open-source-python/intro-to-apis/twitter-data-in-python/
def search_tweet():
    search_words = "#france"
    date_since = "2018-11-16"
    #search only tweets about search words which are the most popular but can look for recent or mixed 
    #we can look for tweets before a certain date with until
    tweets = tw.Cursor(api.search_tweets,
                q=search_words,
                lang="en",
                result_type="mixed").items(5)
    data_sets=[]
    for tweet in tweets:
        #for more information look here: https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/get-search-tweets#example-response
        new_datetime = tweet.created_at.strftime('%Y-%m-%d')
        data_sets.append([tweet.id,new_datetime,tweet.user.name,tweet.user.location,tweet.lang, tweet.text])
    tweet_text = pd.DataFrame(data=data_sets, 
                    columns=['id', "date","user_name","location","language","text"])
    tweet_text.to_json(r'./API/Twitter_API/tweets.json',orient='records')

search_tweet()
