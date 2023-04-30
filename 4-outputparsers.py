from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
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
#print(format_instructions)


template = '''
You will be given a raw string with someone's name. Reformat it as a JSON output containing the keys firstname and lastname, each with the correct value. 

{format_instructions}

% User Input
{input}

Your Response:
'''

prompt  = PromptTemplate(
    input_variables = ['input'],
    partial_variables = {"format_instructions" : format_instructions},
    template = template)

promptValue = prompt.format(input = "Hey I'm Greg. That's my first name. Last name's Johnson.")
#print(promptValue)

llm_output = llm(promptValue)
#print(llm_output)

##print("formatted:")
print(output_parser.parse(llm_output))