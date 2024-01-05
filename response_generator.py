import os

#locate and load environment variables from .env file
from dotenv import find_dotenv, load_dotenv
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
api_key = os.getenv('OPENAI_API_KEY')

#initialize OpenAI client
from openai import OpenAI
client = OpenAI(api_key=api_key)

def generate_story(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a writing assitant, capable of producing thrilling, dramatic, and riveting passages in under 500 words when given a prompt. When given a prompt, do not use words restating the prompt or providing context for the prompt. Simply start the story assuming that the prompt is common knowledge to the reader."},
            {"role": "user", "content": prompt}
        ]
    )
    return completion.choices[0].message.content

#create and print out a test chat completion

