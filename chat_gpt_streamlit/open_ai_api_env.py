import os
from openai import OpenAI
from dotenv import load_dotenv
import os
env_path = os.path.join(".", '.env')
load_dotenv(env_path)
client = OpenAI(
    api_key=os.getenv("Open_ai_key")
)
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Describe the sun in scientific terms",
        }
    ],
    model="gpt-3.5-turbo",
)
print('Hello World! Let\'s send a chat completion request to OpenAI!')
print('\n**Complete Response Object**:\n', chat_completion)
print('\n**Message Response Object**:\n', chat_completion.choices[0].message)
print('\n**Message Response Content**:\n', chat_completion.choices[0].message.content)