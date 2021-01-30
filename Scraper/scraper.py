import re
import sys
import praw
import time
import json
import pprint
import operator
import datetime
from praw.models import MoreComments
from iexfinance.stocks import Stock as IEXStock
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

sub = "wallstreetbets"

with open("config.json") as json_data_file:
    data = json.load(json_data_file)

# create a reddit instance
reddit = praw.Reddit(client_id=data["client_id"],     
                client_secret=data["client_secret"],
                username=data["username"], 
                password=data["password"],
                user_agent=data["user_agent"])


# get 10 hot posts from the MachineLearning subreddit
hot_posts = reddit.subreddit(sub).hot(limit=10)
for post in hot_posts:
    print(post.title)



import pandas as pd
posts = []
ml_subreddit = reddit.subreddit(sub)
for post in ml_subreddit.hot(limit=10):
    posts.append([post.title, post.score, post.id, post.subreddit, post.url, post.num_comments, post.selftext, post.created])
posts = pd.DataFrame(posts,columns=['title', 'score', 'id', 'subreddit', 'url', 'num_comments', 'body', 'created'])
posts