from kor.extraction import create_extraction_chain
from kor.nodes import Object, Text, Number
#langchain
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

#standard helpers
import pandas as pd
import requests
import time
import json
from datetime import datetime
import os

#text helpers
from bs4 import BeautifulSoup
from markdownify import markdownify as md

openai_api_key = os.environ.get("OPENAI_API_KEY")

llm = ChatOpenAI(
    model_name = "gpt-4",
    temperature = 0,
    max_tokens = 2000,
    openai_api_key = openai_api_key
)

person_schema = Object(
    #this will appear in output. it should be the parent of the feilds below. usually singular
    id = "person",
    description = "Personal information about a person",

    attributes = [
        Text(
            id = "firstname",
            description = "the first name of a person",
            )
    ],

    #examples help the model understand what you're talking about
    examples = [
        ("Alice and Bob are friends", [{"first_name": "Alice"}, {"first_name": "Bob"}])
        ]
    )
    
