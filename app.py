
import streamlit as st
from openai import OpenAI
 
st.title("Talk AI")
 
# CHAT HISTORY
 
# Initialize the chat history to empty for every new instance
if "messages" not in st.session_state:
  st.session_state.messages = []
 
# Display the messages from the chat history
for message in st.session_state.messages:
  with st.chat_message(message["role"]):
    st.markdown(message["content"])
 
client = OpenAI(base_url="http://localhost:11434/v1", api_key="random-text")
 
# PROMPT
 
# take user input
prompt = st.chat_input("What's up?")
 
# check if prompt is empty or not. If not empty then display the prompt.
 
if prompt:
  with st.chat_message("user"):
    st.markdown(prompt)
 
  # now add the user prompt to history
  st.session_state.messages.append({"role":"user","content":prompt})
 
 
  # RESPONSE FROM THE ASSISTANT USING LLAMA3 MODEL
 
  with st.chat_message("assistant"):
    stream = client.chat.completions.create(
      model = "llama3",
      messages = [
        {"role": message["role"], "content": message["content"]}
        for message in st.session_state.messages
      ],
      stream=True
    )
    response = st.write_stream(stream)
 
  # add the response in the chat history
  st.session_state.messages.append({"role":"assistant","content":response})
  