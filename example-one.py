import openai
import langchain
import os
import chromadb

openai.api_key = os.environ.get("OPENAI_API_KEY")
print(openai.api_key)

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
print(output)

