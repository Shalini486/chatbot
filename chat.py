import requests

response = requests.post(
  "https://api.inceptionlabs.ai/v1/chat/completions",
  headers={
    "Authorization": "Bearer your_api_key",
    "Content-Type": "application/json"
  },
  json={
    "model": "mercury-2",
    "messages": [
      {"role": "user", "content": "What is the meaning of life?"}
    ]
  }
)

print(response.json())