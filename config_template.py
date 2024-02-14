OPENAI_API_KEY = ""
MODEL_NAME = "gpt-3.5-turbo"
MAX_TOKEN = 4096
TOKEN_THRESHOLD = 250
SYSTEM_TEMPLATE = """
You are configured to talk about a sport named cricket only. 
If you are asked anything about except cricket, 
you don't have to generate anything about it.
"""