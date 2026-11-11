from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
#load settings from .env including the API key
load_dotenv()

#setup the embedding model each text will be represented by 300 numbers
embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)

documents= [
    "Ricky Ponting is one of Australia's greatest cricket captains. He was known for his aggressive batting and excellent leadership.",

    "Steve Smith is a talented Australian batsman known for his unusual batting style and remarkable consistency in Test cricket.",

    "Pat Cummins is a world-class Australian fast bowler. He is known for his accurate bowling, calm personality, and strong leadership.",

    "Glenn Maxwell is an exciting Australian all-rounder famous for his powerful hitting and creative shots, especially in limited-overs cricket.",

    "Shane Warne was a legendary Australian leg-spin bowler. He was famous for his incredible spin, clever bowling tactics, and match-winning performances."    
]

query = "how is maxwell? tell me about him"
#convert documents to 300 numbers using the openai model
document_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)
# Compare the question with every document using cosine similarity.
# [query_embedding] turns one list of 300 numbers into one row of 300 numbers.
# [0] selects that query's row of scores: one score per document.
scores = cosine_similarity([query_embedding], document_embeddings)[0]

best_index, best_score = max(enumerate(scores), key=lambda x: x[1])

print(documents[best_index])
print("Similarity score:", best_score)