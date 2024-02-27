# AI Powered Reddit Bot

## A fully functional reddit bot that uses ChatGPT to generate stories in response to prompts from the r/WritingPrompts subreddit

We have all seen the hundreds of TikToks where text-to-speech reads reddit posts while minecraft parkour or subway surfers plays in the background. This bot is currently a standalone program, however, it serves as a proof-of-concept for the automation of making these TikToks, and demonstates how the first step of finding or generating stories can be automated. This particular bot parses through the r/WritingPrompts subreddit to find a suitable writing prompt, then uses ChatGPT to generate an intriguing story to be posted on the subreddit. 

# Instructions:

This bot is written in Python, so in order to use the bot, you must ensure that your IDE is setup to compile and run Python programs. After setting up your IDE, create a folder that will be your working directory and download all the files in this repository to the folder. Once all the files have been downloaded, you will need to create a virtual environment for the program. This can be done by running the following command and replacing 'YOUR_DIRECTORY' with the directory of the folder you just created:

``
python -m venv YOUR_DIRECTORY
``

Next, You will then need to install three Python packages: PRAW, openai, and dotenv. This can be done by running the following commands:

``
pip install praw
``

``
pip install openai
``

``
python -m pip install python-dotenv
``

After you have installed the above packages, you will now need to obtain a Reddit API key and an OpenAI API key.

## Getting a Reddit API Key:

First make a reddit account, by signing up like a normal user. Once you have setup your reddit account successfully, navigate to the following web address:

``
https://www.reddit.com/prefs/apps/
``

Here, you will login with the account you just created. Once you are logged in, click on the button in the top left corner that reads "are you a developer? create an app..."

<img src ="./images/Screenshot%202024-02-26%20at%207.30.31 PM.png" width=600 height=400>

You will see fields pop up that will allow you to create an API key for your Reddit bot. Choose a name for you bot and select script. In order to create a key, you are required to fill in the redirect url field, however, it doesn't matter what you choose but `http://localhost` is a safe choice. 

<img src ="./images/Screenshot 2024-02-26 at 7.50.50 PM.png" width=600 height=400>

Finally, click "create app" and you should have successfully generated an API key for your Reddit bot. It should look something like this:

<img src ="./images/Screenshot 2024-02-26 at 7.53.26 PM.png" width=600 height=250>

Keep note of the string below "personal use script" which is your app id and your secret. Both of these, highlighted by the red boxes, are needed for the bot to work and will be used later.

## Getting an OpenAI API Key:

Before getting into the steps of creating an OpenAI API key, there is one big caveat to note. When you first make an OpenAI accout, which you have if you've ever used ChatGPT, you are given $18 worth of tokens towards making requests to the OpenAI API. While $18 is a lot and you would have likely never needed to purchase more tokens, unfortunately, these tokens expire after three months since your account creation. This means that if you have already made an OpenAI account, or plan on making a OpenAI account you have only 3 months of using the OpenAI API till you are forced to buy more tokens. Fortunately, for the low price of $5 you can purchase some more tokens that will not expire, and, for use with this reddit bot, $5 is more than enough to last a long time. 

Once you have created an account that has usable tokens, navigate to the following web address:

``
https://platform.openai.com/api-keys
``

Now click on "Create new secret key".

<img src ="./images/Screenshot 2024-02-26 at 7.53.26 PM.png" width=600 height=250>

Simply name your key and then click the green "Create secret key". Leave all permissions.

<img src ="./images/Screenshot 2024-02-26 at 9.10.55 PM.png" width=400 height=250>

You will be given an API key. You must save this key somewhere right now since this is the only time you will be able to see it. If you forgot your key or you didn't save it, you will have to make a new key.

<img src ="./images/Screenshot 2024-02-26 at 9.12.44 PM.png" width=400 height=250>

Now that you have your OpenAI API key, you can now move on to setting up your Reddit bot.

## Setting Up Your Bot

In the folder you created eariler, you will need to create a .env file in the folder which will store all the required keys, secrets, and passwords required for the Reddit Bot. In your .env file, copy and paste the following and replace the text between the quotations with your personal info.

```
CLIENT_ID = "YOUR_REDDIT_APP_ID" 
CLIENT_SECRET = "YOUR_REDDIT_SECRET" 
USERNAME = "YOUR_REDDIT_ACCOUNT_USERNAME" 
PASSWORD = "YOUR_REDDIT_ACCOUNT_PASSWORD"
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
```

You will also need to create a txt file called "posts_replied_to.txt". It is important to ensure that you name the file exactly as I have written it since the program will access this file during its use to check whether or not it has already replied to a post ensuring it doesn't reply to the same post twice.

The setup is now complete!

## Using the Bot

Using the reddit bot is very straight forward. Simply run "main.py" in your terminal and follow the prompts given by the program. I hope you enjoy this program! 

If you have any questions or suggestions for improvement, please feel free to reach out by emailing me at ngoli@umich.edu!