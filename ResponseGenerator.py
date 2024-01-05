import os

#locate and load environment variables from .env file
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
api_key = os.getenv('OPENAI_API_KEY')

#initialize OpenAI client
from openai import OpenAI
client = OpenAI(api_key=api_key)

#create and print out a test chat completion
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "give me three states in the us"},
    ],
    max_tokens=20
)
print(completion.choices[0].message.content)
