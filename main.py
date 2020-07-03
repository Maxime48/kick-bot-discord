# bot.py
import os
import time

import discord
from dotenv import load_dotenv
from discord.utils import get

load_dotenv()
TOKEN = os.getenv('NOPE')

client = discord.Client()
@client.event
async def on_ready():
    print("The bot is ready!")
    await client.change_presence(game=discord.Game(name="Kicking Inactive people"))
    
count = 0
max_sec = 60 
while True: 
    time.sleep(1)
    count += 1
    @client.event
    async def on_ready():
        await client.change_presence(game=discord.Game(name=count))
        if count == max_sec:
            async def purge_members(ctx):
                for member in ctx.message.server.members:
                    if not get(member.roles, name='active'):
                        await bot.kick(member)
            
client.run(TOKEN)
