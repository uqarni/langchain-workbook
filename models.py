import openai
from langchain.schema import Document

import os

openai.api_key = os.environ.get("OPENAI_API_KEY")

template = Document(page_content = "This is my document. It is full of text that I've gathered from other places",
         metadata={
    'id' : 1234,
    'source' : 'Attorney notes',
    'create_time' : 1680013019
         })

print(template)


#Language Model
llm = OpenAI(model_name="text-ada-001", openai_api_key = openai.api_key)
output = llm("What day comes after Friday?")

print(output)


#Chat Model