import praw
import os

#locate and load environment variables from .env file
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)


#initialize reddit bot info
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
username = os.getenv('USERNAME') 
password = os.getenv('PASSWORD')
user_agent = "RedditBot 1.0"

#create an authorized instance of the bot
reddit = praw.Reddit(client_id = client_id,  
                     client_secret = client_secret,  
                     username = username,  
                     password = password, 
                     user_agent = user_agent)

#test that the bot is able to access reddit posts
subreddit = reddit.subreddit('WritingPrompts')
for submission in subreddit.top(limit = 1):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)