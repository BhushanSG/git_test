"""
Here we have integrated openAI's GPT into frontend 
using streamlit.
"""

import streamlit as st

from common_functions import generate_response, num_tokens_from_messages

from config import MODEL_NAME, MAX_TOKEN, TOKEN_THRESHOLD, SYSTEM_TEMPLATE

st.title("💬 Chatbot")

# setting up a list to keep stack of user-input and GPT's output
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "system", "content": SYSTEM_TEMPLATE},
        {"role": "assistant", "content": "How can I help you?"}
    ]

# setting up a loop to inatialize conversation from GPT.
for msg in st.session_state.messages:
    if msg["role"] != "system":
        st.chat_message(msg["role"]).write(msg["content"])

# Taking input from user and generating respose from GPT
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    while True:
        tokens_used = num_tokens_from_messages(st.session_state.messages, MODEL_NAME)
        available_tokens = MAX_TOKEN - tokens_used
        if available_tokens < TOKEN_THRESHOLD:
            st.session_state.messages.pop(1)
        else:
            break
    response = generate_response(st.session_state.messages)
    msg = response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)