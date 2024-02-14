"""
Here we have integrated openAI's GPT into frontend 
using streamlit.
"""
from common_functions import generate_response

from config import  SYSTEM_TEMPLATE


# setting up a list to keep stack of user-input and GPT's output

messages = [
        {"role": "system", "content": SYSTEM_TEMPLATE},
        {"role": "assistant", "content": "How can I help you?"}
]



# Taking input from user and generating respose from GPT
while True:
    prompt = input("Enter prompt:- ")
    messages.append({"role": "user", "content": prompt})
    print("You:- ",prompt)
    response = generate_response(messages)
    msg = response
    messages.append({"role": "assistant", "content": msg})
    print("AI:- ", msg)