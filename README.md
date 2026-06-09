# InceptionLLM Chatbot

This project demonstrates how to interact with the InceptionLLM API (specifically the `mercury-2` model) to build a command-line chatbot.

## Features

- **Conversational Interface**: Maintains context throughout a conversation.
- **System Prompts**: Allows you to define the personality/role of the chatbot.
- **API Integration**: Uses the `requests` library to communicate with the InceptionLLM API.
- **Environment Variables**: Securely manages API keys using `.env` files.

## Getting Started

### Prerequisites

- Python 3.6+
- An API key from InceptionLabs. You can get one from the [InceptionLabs Dashboard](https://dashboard.inceptionlabs.ai/).

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd chatbot
   ```

2. Install dependencies:
   ```bash
   pip install requests python-dotenv
   ```

3. Set up the environment:
   - Create a file named `.env` in the `chatbot` directory.
   - Add your API key to it in the following format:
     ```env
     INCEPTION_API_KEY=your_api_key_here
     ```

## Usage

### Running the Chatbot

To start an interactive chat session, run:

```bash
python3 mychat.py
```

Type your messages and press Enter. The chatbot will respond based on its system prompt.

### Example: Storyteller

The default `mychat.py` uses a system prompt that configures the AI to act as a **storyteller**.

**Sample Interaction:**

```
You: Tell me about a dragon who lost his fire.
Once, in a realm where mountains kissed the clouds, there lived a dragon named Ember...
```

### Changing the System Prompt

Inside `mychat.py`, locate the `my_conversation` list and update the `system` message to change the chatbot's persona:

```python
my_conversation = [
    {
        "role": "system",
        "content": "you are a storyteller"   # Change this to any persona you like
    }
]
```

For example, to make it a **pirate** (as demonstrated in `testchat.py`):

```python
{"role": "system", "content": "You are a pirate."}
```

### API Reference (Quick Look)

We use the `POST /v1/chat/completions` endpoint from InceptionLabs.

**Endpoint:**
```
POST https://api.inceptionlabs.ai/v1/chat/completions
```

**Headers:**
```json
{
  "Authorization": "Bearer your_api_key",
  "Content-Type": "application/json"
}
```

**Request Body:**
```json
{
    "model": "mercury-2",
    "messages": [
        {"role": "system", "content": "..."},
        {"role": "user", "content": "..."}
    ]
}
```

**Response:**
```json
{
    "choices": [
        {
            "message": {
                "content": "..."
            }
        }
    ]
}
```

**Accessing the reply in Python:**
```python
data = response.json()
reply = data["choices"][0]["message"]["content"]
print(reply)
```

## Files Explained

| File | Description |
|------|-------------|
| `mychat.py` | The main application. Loads the API key from `.env`, sets a system prompt (`storyteller`), takes user input, sends the conversation to the API, and prints the response. |
| `chat.py` | A minimal single-turn script to test a basic API call. Uses a hardcoded placeholder key and asks *"What is the meaning of life?"*. Good for verifying your setup. |
| `testchat.py` | A single-turn script demonstrating a custom system persona (pirate). Sends a fixed message and prints just the response content. |
| `.env` | Stores your secret `INCEPTION_API_KEY`. Never commit this file to version control. |

## How `mychat.py` Works — Step by Step

1. **Load environment** — `load_dotenv()` reads `INCEPTION_API_KEY` from `.env`.
2. **Initialize conversation** — A `my_conversation` list is created with the system prompt.
3. **Get user input** — `input("You: ")` captures the user's message.
4. **Append to history** — The user message is added to `my_conversation`.
5. **Send API request** — A `POST` request is made to the InceptionLabs endpoint with the full conversation.
6. **Handle response** — If the response is successful (`response.ok`), the assistant's reply is extracted and printed. Errors are caught and displayed clearly.

## Error Handling

`mychat.py` includes basic error handling:

```python
if response.ok:
    data = response.json()
    if "choices" in data and len(data["choices"]) > 0:
        print(response.json()["choices"][0]["message"]["content"])
    else:
        print("Unexpected response format:", data)
else:
    print(f"Error {response.status_code}: {response.text}")
```

This ensures you get a meaningful message if the API returns an unexpected format or a non-2xx status code.

## Security Note

- **Never hardcode your API key** directly in source files (as seen in `testchat.py` — that key should be rotated immediately).
- Always use `.env` files and add `.env` to your `.gitignore`:
  ```
  .env
  ```

## Future Improvements

- Add a **multi-turn loop** so the conversation continues until the user types `exit`.
- Support **streaming responses** for a more real-time feel.
- Add a **CLI argument** to choose the system persona at runtime.
- Build a simple **web UI** using Flask or Streamlit.
