import praw
import os
from dotenv import find_dotenv, load_dotenv
from response_generator import generate_story

#checks the post for a valid prompt
def check_valid_prompt(prompt):
    if prompt.startswith('[WP]'):
        space_index = prompt.find(' ') 
        new_prompt = prompt[space_index:] 
        prompt = new_prompt
        return True
    else:
        return False

#removes '[WP]' from the post to create a formatted prompt
def format_prompt(prompt):
    space_index = prompt.find(' ') 
    new_prompt = prompt[space_index:] 
    return new_prompt

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

#test that the bot is able to access reddit posts
subreddit = reddit.subreddit('WritingPrompts')
posts_made = 0
for submission in subreddit.hot():
    prompt = submission.title
    if posts_made < 1 and check_valid_prompt(prompt):
        prompt = format_prompt(prompt)
        story = generate_story(prompt)
        print(story)
        posts_made += 1

#allow user to choose length of story and number of stories made
#make it store the pormpts that it has already responded to and not reply to those again
#the stories are currently just longer versions of the prompt, need to find a way to make them more thrilling and not just expansions of the prompt