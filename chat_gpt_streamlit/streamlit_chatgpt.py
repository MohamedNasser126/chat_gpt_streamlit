from openai import OpenAI
import streamlit as st 
import os 

api_key =st.secrets["openai"]["api_key"]
client=OpenAI(api_key=api_key)

def clear_chat():
    st.session_state.chat_history=[{"role":"system","content":"u are a chatbot spcifically designed for answering question regarding the metabolism in bio chemistry"}]
       





def get_chat_response(model_name="gpt-3.5-turbo",temperature=0.7,max_hist_len=10):
    
    
    
    messages_to_send=st.session_state.chat_history[-max_hist_len:]
    stream=client.chat.completions.create(
      messages=messages_to_send,
       model=model_name ,
       stream=True
       ,temperature=temperature
    )
    
    for chunck in stream:
        if chunck.choices[0].delta.content :
            yield chunck.choices[0].delta.content




def main():
    st.title('ASK THE AI')
    
    if ('chat_history' not in st.session_state):
        st.session_state.chat_history=[{"role":"system","content":"u are a chatbot spcifically designed for answering question regarding the metabolism in bio chemistry"}]
    

    model_name=st.sidebar.selectbox("Choose the mode",["gpt-3.5-turbo","gpt-4"],index=0)
    temperature=st.sidebar.slider("set_temp",min_value=0.0,max_value=1.0,value=0.7,step=0.1)
    max_hist_len=int(st.sidebar.number_input("max_hist_len",min_value=0,max_value=10,value=3))

        
    if st.sidebar.button("clear_chat"):
        clear_chat()
    for msg in st.session_state.chat_history:
        if msg["role"] in ["user", "assistant"]:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])
    
    


    
    user_input=st.chat_input("enter your message",key="user_input")
    if user_input:
        st.session_state.chat_history.append({"role":"user","content":user_input})
        with st.chat_message('user'):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            response = st.write_stream(get_chat_response(model_name,temperature,max_hist_len))
            feedback=st.feedback(options='thumbs',key=f"feedback_{len(st.session_state.chat_history)}")
                    
                   
        st.session_state.chat_history.append({"role":"assistant","content":response})
     
    
    

   




                 
        

    
   
if __name__ == "__main__":
    main()