import praw
import datetime
import json

client_id="BPeqBX7V9aPBAQMIZQGHRQ"
secret="S1RvpoYGAefvUGWZY4mPlIjldKZRBg"
user_agent="SDE webscrapping"
def search_post(trends):
    reddit = praw.Reddit(client_id=client_id, client_secret=secret, user_agent=user_agent)
    rows = []

    # if we want more info about the subrreddit (like description) https://praw.readthedocs.io/en/latest/code_overview/models/subreddit.html
    if trends is None:
        trends=["afghanistan","COVID19","FIFA22","dune","dogecoin","squidgame","sports","ethereum","tigerwoods","battlefield2042"]
    else:
        trends = trends.split(',')

    for trend in trends:
        ml_subreddit = reddit.subreddit(trend.strip())
        try:
            for post in ml_subreddit.hot(limit=10):
                post.created=int(post.created)
                timestamp = datetime.datetime.fromtimestamp(post.created)
                name=""
                if(post.author is not None):
                    name=post.author.name

                row = {
                    'id': post.id,
                    'subject': trend,
                    'date': timestamp.strftime('%Y-%m-%d'),
                    'name': post.name,
                    'name_author': name,
                    'score': post.score,
                    'subreddit_name': post.subreddit.display_name,
                    'url': post.url,
                    'num_comments': post.num_comments,
                    'text': post.selftext,

                }
                rows.append(row)
        except:
            continue
            #details about what kind of information we can find in post https://praw.readthedocs.io/en/latest/code_overview/models/submission.html?highlight=num_comments#praw.models.Submission
    
    return rows