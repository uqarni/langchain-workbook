from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI
import os

chat = ChatOpenAI(model = 'gpt-4', temperature = 0, openai_api_key = os.environ.get("OPENAI_API_KEY"))
history = ChatMessageHistory()
history.add_ai_message("hi!")
history.add_user_message("what is the capital of pakistan?")
#print(history.messages)

ai_response = chat(history.messages)
print(ai_response)

history.add_ai_message(ai_response.content)
print(history.messages)
#cool ways to save this as well, not discussed here

