# Testing a single local API request to a locally-running LLM.

import requests
import json

# Start up llama3 at commandline first: 'ollama run llama3'
API_URL = "http://localhost:11434/api/generate"

def chat_with_llama(prompt, api_url=API_URL):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'model': "mrpickles",
        'prompt': prompt,
        'stream': False,
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        result = response.json()
        return result['response']
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

# Example usage
prompt = "Please introduce yourself!"
response = chat_with_llama(prompt)
if response:
    print("LLaMA Response:", response)

