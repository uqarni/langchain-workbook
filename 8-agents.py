#for unknown chains depending on user inputs

# agent - language model driving the decision making
# tool - a capability of an agent. eg google search
#toolkit - a group of tools your agent can select from
import os
from langchain.agents import load_tools
from langchain.agents import initialize_agent
from langchain.llms import OpenAI
import json
llm = OpenAI(temperature = 0, openai_api_key = os.environ.get("OPENAI_API_KEY"))

serpapi_key = os.environ.get("SERP_API_KEY")

toolkit = load_tools(["serpapi"], llm = llm, serpapi_api_key = serpapi_key)
# different types of agents for different types of tasks
agent = initialize_agent(toolkit, llm, agent = "zero-shot-react-description", verbose = True, return_intermediate_steps = True)

response = agent({"input": "what is the sales tax on groceries in Oklahoma? Does it vary by city or county?"})
print(json.dumps(response["intermediate_steps"], indent = 2))