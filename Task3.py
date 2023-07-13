import os
from langchain.llms import OpenAI
from langchain import ConversationChain
from langchain import PromptTemplate

def chatBot():

    """This function takes user inputs and reply as an AI bot. The bot will make
        a joke about your name if you tell it your name in the second text"""

    #Initializing my OpenAI key
    os.environ['OPENAI_API_KEY'] = 'key' #Edit this to your OpenAI key

    #Initializing the model that we will use. (text-davinci-003 corressponds to turbo-3.5-gpt)
    llm = OpenAI(model_name = "text-davinci-003")

    #Using a chain for remembering the texts
    conversation = ConversationChain(llm = llm, verbose = True)

    #Sample Texts
    output = conversation.predict(input = input())
    print(output)

    # Using a promt tempelate to make jokes about users' name.
    prompt = PromptTemplate(
    input_variables=["name"],
    template="Write a joke about my name. {name}",
    )

    formatted = prompt.format(name = input())
    output = conversation.predict(input = formatted)
    print(output)

    #To demonstrate that it remember's the texts
    output = conversation.predict(input = input())
    print(output)

if __name__ == "__main__":

    """Driver function"""
    chatBot()
