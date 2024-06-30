# A simple chatbot to connect to a discord server.
# It assumes there's an LLM running on localhost.
# It only speaks when directly messaged in a channel.

# Current authorization token -- this can be reset on dev portal.
BOT_TOKEN = "" # FILL THIS OUT!

import discord
import os
import requests
import json

# Start up llama3 at commandline first: 'ollama run llama3'
API_URL = "http://localhost:11434/api/generate"


# Assumes our LLM personality is running on localhost.
def chat_with_llm(prompt, api_url=API_URL):
    headers = {
        'Content-Type': 'application/json',
    }
    data = {
        'model': "mrpickles", # See the MODELFILE for personality!
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

# Creates the Discord chatbot
intents = discord.Intents.default()
intents.message_content = True  # Enable the intent to read message content
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:

        spoken = message.content.split(" ", 1)[1] # remove the <@39839> prefix junk
        print(f"Received content: " + spoken)
        
        if 'hello' in message.content.lower():
            await message.channel.send('Hello!')
        elif 'ping' in message.content.lower():
            await message.channel.send('Pong!')
        else:
            #answer = "I heard you say: '" + spoken + "'. But I need MOAR cheese!"
            response = chat_with_llm(spoken)
            if response:
                await message.channel.send(response)
            else:
                await message.channel.send("LLM ERROR")

    
client.run(BOT_TOKEN)


