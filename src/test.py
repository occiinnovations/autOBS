import requests
from dotenv import load_dotenv
import os

load_dotenv()

while True:
    num = input("Enter integer to trigger: ")
    if num.lower() == 'exit':
        break

    # This automatically shoots the number to the main server
    requests.post(f"http://{os.getenv("my_HOST")}:{os.getenv("my_API_PORT")}/{num}")
