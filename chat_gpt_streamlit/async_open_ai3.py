from openai import OpenAI
import os
from dotenv import load_dotenv
import asyncio
env_path=os.path.join('.','.env')
load_dotenv(env_path)

client=OpenAI(api_key=os.getenv("Open_ai_key"))

stream=client.chat.completions.create(
    messages=[
        {"role": "user",
            "content": "Describe the sun in scientific terms"}

    ]
    ,model='gpt-3.5-turbo',
    stream=True
)

for chunk in stream :
    print(chunk.choices[0].delta.content or "",end="")