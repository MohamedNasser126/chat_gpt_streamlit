from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import asyncio

env_path=os.path.join('.','.env')
load_dotenv(env_path)

client=AsyncOpenAI(api_key=os.getenv('Open_ai_key'))

async def fetch_chat_completion():
    chat_completion=await client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user',
                   'content':'Describe the sun in scientific terms'}]
    )
    print('\n**response ready**\n',chat_completion.choices[0].message.content)

async def main():
    print("Hello World! Let's send a chat completion request to OpenAI!")
    task=asyncio.create_task(fetch_chat_completion())
    
    print('I am not blocked with the chat completion task!')
    
    await task


asyncio.run(main())