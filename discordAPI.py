import discord
from discord.ext import commands

#Defining intents as default
intents = discord.Intents.default()
intents.message_content = True

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
bot.run('MTEyODY5Nzc1ODU5ODA0NTcwNg.GhfIcc.4iJHmY_CoLG4IDlD5_NAafT0ee-fvSlYeOBu2Y')