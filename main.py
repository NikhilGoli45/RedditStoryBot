from reddit_bot import *

#Welcomes the user to he bot
welcome_msg = "Welcome to the Reddit Story Bot!\n"
welcome_msg += "I am a bot creates AI generated stories in response to writing prompts from the r/WritingPrompts subreddit.\n"
print(welcome_msg)

#asks user to generate story
while True:
    user = input("Would you like to generate a story?\n")
    if user in yesresponse:
        prompt = find_prompt()
        user = input("Would you like to generate another story?\n")
    elif user in noresponse:
        print("\nThank you for using the Reddit Story Bot!\n")
        break
    else:
        user = print("\nI didn't understand that.\n")
exit()
