
import praw
import pandas as pd
import datetime

client_id="BPeqBX7V9aPBAQMIZQGHRQ"
secret="S1RvpoYGAefvUGWZY4mPlIjldKZRBg"
user_agent="SDE webscrapping"
def search_post():
    reddit = praw.Reddit(client_id=client_id, client_secret=secret, user_agent=user_agent)
    posts = []
    # if we want more info about the subrreddit (like description) https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
    ml_subreddit = reddit.subreddit('MachineLearning')
    for post in ml_subreddit.hot(limit=10):
        post.created=int(post.created)
        timestamp = datetime.datetime.fromtimestamp(post.created)
        new_datetime = timestamp.strftime('%Y-%m-%d')
        #details about what kind of information we can find in post https://praw.readthedocs.io/en/latest/code_overview/models/submission.html?highlight=num_comments#praw.models.Submission
        posts.append([post.id,new_datetime,post.title,post.author.name, post.score, post.subreddit.display_name, post.url, post.num_comments, post.selftext ])
    posts = pd.DataFrame(data=posts,columns=['id', 'date', 'name','name_author','score', 'subreddit_name', 'url', 'num_comments', 'text'])
    posts.to_json(r'./API/Reddit_API/post.json',orient='records',default_handler=str)
search_post()
