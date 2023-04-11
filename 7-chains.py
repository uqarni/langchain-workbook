# combining different LLM calls and action automatically
import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.chains import SimpleSequentialChain


#####Simple Sequential Chain
llm = OpenAI(temperature = 1, openai_api_key = os.environ.get("OPENAI_API_KEY"))

template1 = """
Your job is to come up with a classic dish from the area that the user suggests.
%USER LOCATION
{user_location}

YOUR RESPONSE:
"""

prompt_template1 = PromptTemplate(input_variables=["user_location"], template =template1)

# Holds my 'location' chain
location_chain = LLMChain(llm = llm, prompt = prompt_template1)

template2 = """
Given a meal, give a short and simple recipe on how to amke that dish at home.
%MEAL
{user_meal}

YOUR RESPONSE:
"""

prompt_template2 = PromptTemplate(input_variables = ["user_meal"], template = template2)

#holds my 'meal' chain
meal_chain = LLMChain(llm = llm, prompt = prompt_template2)

#combine into a chain
overall_chain = SimpleSequentialChain(chains=[location_chain, meal_chain], verbose=True)
#example = overall_chain.run("Pakistan")

####Summarization Chain
#Run through long documents and get a summary

from langchain.chains.summarize import load_summarize_chain
from langchain.document_loaders import TextLoader  
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = TextLoader('/meditations.txt')
documents = loader.load()

#get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)

#split your doc
texts = text_splitter.split_documents(documents)

#run summarization
chain = load_summarize_chain(llm, chain_type = "map_reduce", verbose = True)
chain.run(texts)
