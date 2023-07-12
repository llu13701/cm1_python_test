import os
from langchain.llms import OpenAI
from langchain import ConversationChain
from langchain import PromptTemplate

#Initializing my OpenAI key
os.environ['OPENAI_API_KEY'] = 'Key' #Edit this to your key

#Initializing the model that we will use. (text-davinci-003 corressponds to turbo-3.5-gpt)
llm = OpenAI(model_name = "text-davinci-003")

#Using a chain for remembering the texts
conversation = ConversationChain(llm = llm, verbose = True)

#Sample Texts
output = conversation.predict(input = "Hello")
print(output)

# Using a promt tempelate to make jokes about users' name.
prompt = PromptTemplate(
 input_variables=["name"],
 template="Write a joke about my name. {name}",
)

formatted = prompt.format(name = "My name is Rajat")
output = conversation.predict(input = formatted)
print(output)

#To demonstrate that it remember's the texts
output = conversation.predict(input = "What was my first text in this conversation")
print(output)