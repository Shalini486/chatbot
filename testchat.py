import requests

response = requests.post(
  "https://api.inceptionlabs.ai/v1/chat/completions",
  headers={
    "Authorization": "Bearer sk_ec801f0f07cc2e5772b9df63cfefc455",
    "Content-Type": "application/json"
  },
  json={
    "model": "mercury-2",
    "messages": [
      {"role": "system", "content": "You are a pirate."},
      {"role": "user", "content": "Tell me a joke"}
    ]
  }
)

print(response.json()["choices"][0]["message"]["content"],end="")