from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding =OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

documents = [
    "Oslo is the capital of norway"
    "Washington Dc is the capital of the united states"
    "Cape Town is the capital of South Africa"
]

result = embedding.embed_documents(documents)

print(str(result))
