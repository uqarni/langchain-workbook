import openai
import os
from langchain.document_loaders import HNLoader

#####loaders; like Plugins
#someone made a hacker news loader
loader = HNLoader("https://news.ycombinator.com/item?id=35301943")

data = loader.load()
# print(f"Found{len(data)} comments")
# print(data[:5])



#####TextSplitters; there are many kinds
from langchain.text_splitter import RecursiveCharacterTextSplitter

with open('meditations.txt') as doc:
    meditations = doc.read()

#just one long piece of text here
# print(f"you have {len([meditations])} document")

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 150,
    chunk_overlap = 20,)

#splits it into little docs
text = text_splitter.create_documents([meditations])
#print(f"you have {len(text)} documents")

# print("preview:")
# print(text[500].page_content, "\n")
# print(text[1000].page_content)


######Retreivers
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = TextLoader('meditations.txt')
meditations = loader.load()

#get splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 50)

#split doc into texts
texts = text_splitter.split_documents(meditations)

#get embeddings engine ready
embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get("OPENAI_API_KEY"))

#embed texts
db = FAISS.from_documents(texts,embeddings)

#initalize your retreiver; asking for just 1 doc back
retriever = db.as_retriever()

# print(retriever)

docs = retriever.get_relevant_documents("what habits make for a great man?")
#print("\n\n".join([x.page_content[:200] for x in docs[:5]]))




#####VectorStores
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

loader = TextLoader('meditations.txt')
documents = loader.load()

#get your splitter ready
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 50)

#split your doc into texts
texts = text_splitter.split_documents(documents)

#get embeddings engine ready
embeddings = OpenAIEmbeddings(openai_api_key = os.environ.get("OPENAI_API_KEY"))

print(f"you have {len(texts)} documents")

embedding_list = embeddings.embed_documents([text.page_content for text in texts])
print(f"You have {len(embedding_list)} embeddings")
print(f"here is a sample of one: {embedding_list[0][:3]}...")


