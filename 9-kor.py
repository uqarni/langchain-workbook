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
    
chain = create_extraction_chain(llm, person_schema)

text = "My name is Bobby. My sister's name is Rachel. My brother's name is Joe. My dog's name is Spot."
#output = chain.predict_and_parse(text = (text))["data"]
#print(output)

#output = chain.predict_and_parse(text = "The dog went to the park")["data"]
#print(output)

plant_schema = Object(
    id="plant",
    description = "Information about a plant",

    attributes = [
        Text(
            id = "plant_type",
            description = "The common name of the plant",
        ),
        Text(
            id = "color",
            description = "The color of the plant",
        ),
        Number(
            id = "rating",
            description = "The rating of the plant",
        )
    ],
    examples = [
        (
            "Roses are red, lilies are white and an 8 out of 10",
            [
            {"plant_type": "roses", "color": "red"},
            {"plant_type": "lilies", "color": "white", "rating": 8},
            ],
        )
    ]
)

text = "Plan trees are brown with a 6 rating.. Sequioa trees are green."

chain = create_extraction_chain(llm, plant_schema)
#output = chain.predict_and_parse(text = text)["data"]
#print(output)

parts = Object(
    id = "parts",
    description = "Parts of a car",
    attributes = [
        Text(id = "part", description = "The name of the part of a car")
    ],
    examples=[
        ("the jeep has wheels and windows", 
            [
                {"part": "wheels"},    
                {"part": "windows"}
            ],
        )
    ]
)

cars_schema = Object(
    id = "car",
    description = "Information about a car",
    examples = [
        (
            "the bmw is red and has an engine and steering wheel",
            [
                {"type": "BMW", "color": "red", "parts": ["engine", "steering wheel"]}
            ],
        )
    ],
    attributes=[
        Text(
            id = "type",
            description = "The make or brand of car",
        ),
        Text(
            id = "color",
            description = "The color of the car",
        ),
        parts
    ]
)

text = "The blue Mercedes Benze has a rearview mirror, roof, and windwhield. Inside sits a girl wearing pants. On those pants she's wearing a huge Texan leather belt."

chain = create_extraction_chain(llm, cars_schema, encoder_or_encoder_class = "json")
#output = chain.predict_and_parse(text = text)["data"]
#print(output)

#the prompt is pretty interesting. kor does this
#prompt = chain.prompt.format_prompt(text = text).to_string()
#print(prompt)

schema = Object(
    id = "forecaster",
    description=