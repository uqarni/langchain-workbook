import openai
import os
from langchain.document_loaders import HNLoader

#loaders; like Plugins
#someone made a hacker news loader
loader = HNLoader("https://news.ycombinator.com/item?id=35301943")

data = loader.load()
print(f"Found{len(data)} comments")
print(data[:5])



#TextSplitters
from langchain.text_splitter import RecursiveCharacterTextSplitter
