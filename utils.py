import os
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
def load_env():
    dotenv_file = find_dotenv()
    if not dotenv_file:
        raise FileNotFoundError(".env file not found. Make sure it exists in the expected directory.")
    load_dotenv(dotenv_file)

# Retrieve OpenAI API key from environment variables
def get_openai_api_key():
    load_env()
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file. Please ensure it's correctly set.")
    return openai_api_key

# Test the key retrieval
if __name__ == "__main__":
    try:
        api_key = get_openai_api_key()
        print("OpenAI API Key successfully retrieved:", api_key)
    except Exception as e:
        print("Error:", str(e)) 
