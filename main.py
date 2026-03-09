import discord
import os
import threading
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Discord bot is running"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send("Hello! I'm an echobot, give it a try.")
    else:
        await message.channel.send(message.content)

def run_bot():
    client.run(os.getenv('TOKEN'))

thread = threading.Thread(target=run_bot, daemon=True)
thread.start()
