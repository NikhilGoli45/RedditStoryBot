from reddit_bot import *

#Welcomes the user to the bot
welcome_msg = "Welcome to the Reddit Story Bot!\n"
welcome_msg += "I am a bot creates AI generated stories in response to writing prompts from the r/WritingPrompts subreddit.\n"
print(welcome_msg)

#asks user to generate story
user = input("Would you like to generate a story?\n")
while True:
    if user in yesresponse:
        prompt = make_post()
        user = input("\nWould you like to generate another story?\n")
    elif user in noresponse:
        print("\nThank you for using the Reddit Story Bot!\n")
        break
    else:
        user = print("\nI didn't understand that. Please enter 'yes' or 'no'\n")
exit()
