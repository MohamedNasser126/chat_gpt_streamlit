from openai import AsyncOpenAI
import os
from dotenv import load_dotenv
import asyncio

env_path=os.path.join('.','.env')
load_dotenv(env_path)
client=AsyncOpenAI(api_key=os.getenv("Open_ai_key"))
async def main():
    stream=await client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[{'role':'user',
         'content':'Describe the sun in scientific terms'}],
         stream=True
    )
    async for chunck in stream:
        print(chunck.choices[0].delta.content or "",end="")
asyncio.run(main())