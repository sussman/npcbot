# npcbot
a Discord chatbot that speaks to a locally-running LLM personality.

As originally designed and built, it assumes that both the chatbot and LLM are running on the same local machine.  Everything was originally done on an Apple-Silicon Mac.

### Instructions

- Install [ollama](https://ollama.com/) and download the latest llama3 model ("ollama get llama3")
- Create the LLM personality from a MODEL file included here
  - ollama create mrpickles -f ./MODEL-PICKLES
  - ollama run mrpickles
- Create yourself a "bot" application on the Discord [developer site](https://discordpy.readthedocs.io/en/stable/discord.html), and invite it to join your Discord server.
- Back on your local machine, run "python ./npcbot.py" to run the bot client.
    - It connects to Discord, waiting to answer any requests coming from your server channel.
    - Make sure the python script is requesting the proper ollama model in its local HTTP call (e.g. 'model':'mrpickles')

