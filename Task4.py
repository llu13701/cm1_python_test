import discord
from discord.ext import commands
import nest_asyncio
import asyncio

def discordBot():

    """This function creates a simple bot to say "Hello {user_name}!" 
        to every new incoming message in a discord server"""

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


    def run_bot():

        """This function routes to our bot by using bot's token"""

        bot.run('Key') #Edit this to your discord key

    #This lets asyincio to be called when other asyncio event is running in the Jupyter Notebook
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())

if __name__ == "__main__":

    """Driver Function"""
    discordBot()
