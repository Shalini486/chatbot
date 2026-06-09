import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("INCEPTION_API_KEY")

my_conversation = [
    {
        "role": "system",
        "content": "you are a storyteller"
    }
]

user_msg = input("You: ")
my_conversation.append({"role": "user", "content": user_msg})

response = requests.post(
    "https://api.inceptionlabs.ai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "mercury-2",
        "messages": my_conversation
    }
)

if response.ok:
    data = response.json()
    if "choices" in data and len(data["choices"]) > 0:
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print("Unexpected response format:", data)
else:
    print(f"Error {response.status_code}: {response.text}")