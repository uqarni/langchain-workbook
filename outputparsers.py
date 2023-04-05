from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain.llms import OpenAI
import openai
import os

#two main concepts:
#Format Instructions - how we want our responses formatted
#parser - method to extract results into desired file type (csv or json)

openai.api_key = os.environ.get("OPENAI_API_KEY")
openaikey = openai.api_key

llm = OpenAI(model = "text-davinci-003", openai_api_key = openaikey)


response_schema = [
    ResponseSchema(name = "input", description = "raw input of names"),
    ResponseSchema(name = "output", description = "JSON format of first and last names")
]

output_parser = StructuredOutputParser.from_response_schemas(response_schema)

format_instructions = output_parser.get_format_instructions()
print(format_instructions)


template = '''
You will be given a raw string 
'''