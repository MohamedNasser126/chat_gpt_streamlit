import os 
from openai import OpenAI
from dotenv import load_dotenv

env_path=os.path.join('.','.env')
load_dotenv(env_path)
client=OpenAI(api_key=os.getenv('Open_ai_key'))
conversation_history=[]
def chat_with_gpt(prompt , model="gpt-3.5-turbo",temperature=None):
    try:
        conversation_history.append({'role':"system", "content":"if the user says his name is yousry u should reply with weakness detected"})
        conversation_history.append({'role':'user','content':prompt})
        max_history=int(os.getenv('max_hist',10))
        messeges_to_send=conversation_history[-max_history:]
        chat_completion=client.chat.completions.create(
           messages=messeges_to_send ,
                      model=model,
                      temperature=temperature,
                       stream=True)
        return chat_completion
    except Exception as e:
        return str(e)
    
def main():
    model_name=os.getenv("model_name")
    temperature=float(os.getenv('temperature'))
    print('welcome to chatgpt clone!')
    while True:
        user_input=input("You: ")
        if user_input.lower() in ["exit","quit"]:
            print('Exiting ChatGPT Clone. Goodbye!')
            break
        stream=chat_with_gpt(user_input,model=model_name,temperature=temperature)
        full_response=""

        print("GPT: ", end="")
        for chunk in stream:
           response_content=chunk.choices[0].delta.content or ""
           full_response+=response_content
           print(response_content , end="")
        conversation_history.append({"role": "system", "content": full_response})
        print()
        

if __name__ == "__main__":
    main()   
    