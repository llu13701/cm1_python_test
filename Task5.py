import discord
from discord.ext import commands
import nest_asyncio
import asyncio
import os
from langchain.llms import OpenAI
from langchain import ConversationChain
from langchain import PromptTemplate

def discordBot():

    """This function creates a discord AI bot that responds to a text for:
        1. Sending greetings to the user who sends the message.
        2. Sending a joke about the user's name.
        3. Answering any query that the user might have."""

    #Initializing my OpenAI key
    os.environ['OPENAI_API_KEY'] = 'KEY' #Edit this to your OpenAI key

    #Initializing the model that we will use. (text-davinci-003 corressponds to turbo-3.5-gpt)
    llm = OpenAI(model_name = "text-davinci-003")
    conversation = ConversationChain(llm = llm, verbose = True) #Using a chain for remembering the texts

    # Using a promt tempelate to make jokes about users' name.
    prompt = PromptTemplate(
    input_variables=["name"],
    template="Write a joke about my name. {name}",
    )

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

        #Addidng exeception for the bot's own texts
        if message.author == bot.user:
            return
        
        #Sending initial greetings to the user
        text = conversation.predict(input = "Hello")
        await message.channel.send(f'{text}')
        
        #Sending texts about jokes on user's name
        formatted = prompt.format(name = f'My name is {message.author.name}')
        text = conversation.predict(input = formatted)
        await message.channel.send(f'{text}')

        #Sending texts about any questions that the user might have
        text = conversation.predict(input = message.content)
        await message.channel.send(f'{text}')

    #Defining our bot's token
    def run_bot():
        bot.run('Key') #Edit this to your discord key

    #This lets asyincio to be called when other asyncio event is running in the Jupyter Notebook
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run_bot())

if __name__ == "__main__":
    
    """Driver function"""
    discordBot()