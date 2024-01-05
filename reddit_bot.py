import praw
import os
from dotenv import find_dotenv, load_dotenv
from response_generator import generate_story

#loads previously replied to posts
def load_posts_replied_to():
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
    return posts_replied_to

#checks the post for a valid prompt
def check_valid_prompt(submission):
    posts_replied_to = load_posts_replied_to()
    if submission.title.startswith('[WP]') and submission.id not in posts_replied_to:
        return True
    else:
        return False

#removes '[WP]' from the post to create a formatted prompt
def format_prompt(submission):
    prompt = submission.title
    space_index = prompt.find(' ') 
    new_prompt = prompt[space_index:] 
    return new_prompt

#saves post id and replies to post with the gpt generated story
def post_story(submission, story):
    posts_replied_to = load_posts_replied_to()
    posts_replied_to.append(submission.id)
    with open("posts_replied_to.txt", "w") as f:
        for submission_id in posts_replied_to:
            f.write(submission_id + "\n")
    submission.reply(story)

#locate and load environment variables from .env file
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

#make the post
subreddit = reddit.subreddit('WritingPrompts')
posts_made = 0
for submission in subreddit.hot():
    if posts_made < 1 and check_valid_prompt(submission):
        prompt = format_prompt(submission)
        story = generate_story(prompt)
        post_story(submission, story)
        posts_made += 1

#allow user to choose length of story and number of stories made
#the stories are currently just longer versions of the prompt, need to find a way to make them more thrilling and not just expansions of the prompt