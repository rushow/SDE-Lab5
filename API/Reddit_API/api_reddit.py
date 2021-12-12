
import praw
import pandas as pd
import datetime
import json

client_id="BPeqBX7V9aPBAQMIZQGHRQ"
secret="S1RvpoYGAefvUGWZY4mPlIjldKZRBg"
user_agent="SDE webscrapping"
def search_post():
    final_dataset=[]
    reddit = praw.Reddit(client_id=client_id, client_secret=secret, user_agent=user_agent)
    posts = []
    # if we want more info about the subrreddit (like description) https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
    trending=["afghanistan","COVID19","FIFA22","dune","dogecoin","squidgame","sports","ethereum","tigerwoods","battlefield2042"]
    for trends in trending:
        print(trends)
        ml_subreddit = reddit.subreddit(trends)
        for post in ml_subreddit.hot(limit=100):
            post.created=int(post.created)
            timestamp = datetime.datetime.fromtimestamp(post.created)
            new_datetime = timestamp.strftime('%Y-%m-%d')
            name=""
            if(post.author==None):
                name=""
            else:
                name=post.author.name
            #details about what kind of information we can find in post https://praw.readthedocs.io/en/latest/code_overview/models/submission.html?highlight=num_comments#praw.models.Submission
            posts.append([post.id,trends,new_datetime,post.title,name, post.score, post.subreddit.display_name, post.url, post.num_comments, post.selftext ])
        posts = pd.DataFrame(data=posts,columns=['id','subject', 'date', 'name','name_author','score', 'subreddit_name', 'url', 'num_comments', 'text'])
        final_dataset.append(posts)
    final_dataset=pd.concat(final_dataset)
    final_dataset.to_json(r'./API/Reddit_API/post.json',orient='records',default_handler=str)
def utf_correction():
    tweets=[]
    with open("./API/Reddit_API/post.json") as jsonFile:
        for jsonObj in jsonFile:
            tweet = json.loads(jsonObj)
            tweets.append(tweet)
        jsonFile.close()
    with open("./API/Reddit_API/post_corect.json","w",encoding='utf-8') as jsonFile:
        for tweet in tweets:
            json.dump(tweet,jsonFile,ensure_ascii=False)
#search_post()
utf_correction()
