# bot.py
import os

import discord
from dotenv import load_dotenv

print("UR MOM GAY")

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

client.run('token', 'Njc3NDQzODEwNzAzMzEwODYy.XkUgng.PRPYfKcPA2q9Sn6hy1OEFY2JguU')
