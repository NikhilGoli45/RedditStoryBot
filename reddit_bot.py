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
    return submission.title.startswith('[WP]') and submission.id not in posts_replied_to


#removes '[WP]' from the post to create a formatted prompt
def format_prompt(submission):
    prompt = submission.title
    space_index = prompt.find(' ') 
    new_prompt = prompt[space_index:] 
    return new_prompt

#saves post id and replies to post with the gpt generated story
def post_story(submission, story):
    user = input("\nWould you like to post this story on the r/WritingPrompts subreddit?\n")
    while True:
        if user in yesresponse:
            print("\nAwesome! Please wait while I post your story...\n")
            posts_replied_to = load_posts_replied_to()
            posts_replied_to.append(submission.id)
            with open("posts_replied_to.txt", "w") as f:
                for submission_id in posts_replied_to:
                    f.write(submission_id + "\n")
            submission.reply(story)
            print("Your story has been successfully posted.\nYou can view it here:\n\nhttps://www.reddit.com" + submission.permalink + "\n")
            return
        elif user in noresponse:
            print("Sorry to hear that. I hope you will post the next story you generate!")
            return
        else:
            user = input("I didn't understand that. Please answer 'yes' or 'no'.\n")
        
#Asks if the user is satisifed with the prompt found by the bot
def approve_prompt(prompt):
    print("\n" + prompt + "\n")
    while True:
        user_approval = input("Is this prompt good?\n")
        if user_approval in yesresponse:
            print("\nGreat!\n")
            return True
        elif user_approval in noresponse:
            print("\nNo worries, I will find another prompt.\n")
            return False
        else:
            print("\nPlease answer 'yes' or 'no'.\n")

#searches for a satisfactory prompt for the user
def make_post():
    print("\nFantastic! Please wait while I find a prompt.\n")
    subreddit = reddit.subreddit('WritingPrompts')
    for submission in subreddit.hot():
        if check_valid_prompt(submission):
            prompt = format_prompt(submission)
            if approve_prompt(prompt):
                print("Please wait while I generate your story...\n")
                story = generate_story(prompt)
                print("Here is your story:\n\n" + story)
                post_story(submission, story)
                return

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

yesresponse = {"yes", "Yes", "YES", "y", "Y"}
noresponse = {"no", "No", "NO", "n", "N"}