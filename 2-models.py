import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

##Language Model
from langchain.llms import OpenAI
llm = OpenAI(model_name="text-ada-001", openai_api_key = openai.api_key)
output = llm("What's the shortest month of the year?")

#print(output)


##Chat Models
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


##Embeddings Models
from langchain.embeddings import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(openai_api_key = openai.api_key)

text = "Hi! Do you offer patents?"

text_embedding = embeddings.embed_query(text)
#print(f"Your embedding's length is {len(text_embedding)}")
#print(f"First few entries in it are {text_embedding[:3]}...")



