"""
Here we have integrated openAI's GPT into frontend 
using streamlit.
"""
from common_functions import generate_response,num_tokens_from_messages
from config import  SYSTEM_TEMPLATE,MODEL_NAME,MAX_TOKEN,TOKEN_THRESHOLD


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
    while True:
        tokens_used = num_tokens_from_messages(messages, MODEL_NAME)
        available_tokens = MAX_TOKEN - tokens_used
        if available_tokens < TOKEN_THRESHOLD:
            messages.pop(1)
        else:
            break
    response = generate_response(messages)
    msg = response
    messages.append({"role": "assistant", "content": msg})
    print("AI:- ", msg)