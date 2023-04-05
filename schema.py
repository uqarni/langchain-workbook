import openai
import langchain
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")


#Chat Schema
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature = 0, openai_api_key = openai.api_key)

output = chat(
    [
    SystemMessage(content="You are a nice AI bot that helps a user figure out what to eat in a short sentence."),
    HumanMessage(content="I like tomatoes, what should I eat?"),
    AIMessage(content="Try caprese salad with fresh mozzarella"),
    HumanMessage(content="I don't like cheese")
    ]
)

#Document Schema
from langchain.schema import Document

template = Document(page_content = "This is my document. It is full of text that I've gathered from other places",
         metadata={
    'id' : 1234,
    'source' : 'Attorney notes',
    'create_time' : 1680013019
         })

print(template)
print(output)

