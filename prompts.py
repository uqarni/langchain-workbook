from langchain.llms import OpenAI
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")
openaikey = openai.api_key


## Simple Prompt
llm = OpenAI(model_name="text-davinci-003", openai_api_key = openaikey)

prompt = '''
Today is Wednesday, I'll get back to you tomorrow which is Saturday.
What's wrong with this sentence?
'''

# output = llm(prompt)
# print(output)

##Prompt Templates
from langchain.llms import OpenAI
from langchain import PromptTemplate

llm = OpenAI(model_name="text-davinci-003", openai_api_key = openaikey)

template = '''
I live in {start} and want to go on vacation to {end}. What's the best way to get there?
Response in one short sentence.
'''

prompt = PromptTemplate(
    input_variables = ["start", "end"],
    template = template
)

final_prompt = prompt.format(start = "Chicago", end = "the Moon")

# print(f"actual prompt: {final_prompt}")
# print(f"answer: {llm(final_prompt)}")



##Example Selectors
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import FewShotPromptTemplate, PromptTemplate
from langchain.llms import OpenAI

llm = OpenAI(model_name = "text-davinci-003", openai_api_key = openaikey)

example_prompt = PromptTemplate(
    input_variables = ["input", "output"],
    template = "Example Input: {input} \nExample Output: {output}",
)

#examples of the color of certain objects
examples = [
    {"input": "orange fruit", "output": "orange"},
    {"input": "firetruck", "output": "red"},
    {"input": "cloud", "output": "white"},
    {"input": "wood", "output": "brown"},
    {"input": "steel", "output": "gray"},
    {"input": "coal", "output": "black"},
]

example_selector = SemanticSimilarityExampleSelector.from_examples(
    examples,
    OpenAIEmbeddings(openai_api_key = openaikey),
    FAISS, #vectorstore class used to store embeddings; pip install faiss-cpu
    k = 2 #number of examples to product
)

similar_prompt = FewShotPromptTemplate(
    #the object that will help us select examples
    example_selector = example_selector,
    #our prompt
    example_prompt = example_prompt,
    #cusotmizations that we'll add before and after
    prefix = "Give the color of the item",
    suffix = "Input: {input} \nOutput:",

    #what the input will get for the variable
    input_variables = ["input"],
)


#choose the input
obj = "grass"
print(similar_prompt.format(input = obj))

output = llm(similar_prompt.format(input = obj))
print(output)

