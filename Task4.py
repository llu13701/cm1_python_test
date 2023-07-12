
import discord
from discord.ext import commands
import nest_asyncio
import asyncio

#Using nest_asyncio for Jupyter notebook
nest_asyncio.apply()

#Defining intents as default
intents = discord.Intents.default()
intents.message_content = True

#Initializing the bot
bot = commands.Bot(command_prefix='!', intents=intents)

#Decorator to send messages
@bot.event
async def on_message(message):

    #Addidng exeception for the bot to not say hello to itself
    if message.author == bot.user:
        return
    
    #Message to say Hello {username}!
    await message.channel.send(f'Hello {message.author.name}!')

#Defining our bot's token
def run_bot():
    bot.run('Key') #Edit this to your key

#This lets asyincio to be called when other asyncio event is running in the Jupyter Notebook
loop = asyncio.get_event_loop()
loop.run_until_complete(run_bot())
