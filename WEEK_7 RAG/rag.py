import os

import chromadb
from dotenv import load_dotenv
from google import genai


# Load environment variables
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

print("API Key loaded:", api_key is not None)


# Create clients
gemini_client = genai.Client(api_key=api_key)
chroma_client = chromadb.Client()

print("Clients created successfully!")


# Create ChromaDB collection
collection = chroma_client.get_or_create_collection(
    name="rag_collection"
)


# Documents
documents = [
    "FastAPI is a Python framework for building APIs.",
    "ChromaDB is a vector database.",
    "Python is a programming language.",
    "ChromaDB stores vector embeddings."
]


# Store documents in ChromaDB
collection.add(
    documents=documents,
    ids=["1", "2", "3", "4"]
)

print("Documents added successfully!")


# Get user question
question = input("\nAsk your question: ")


# Retrieve top 2 relevant documents
results = collection.query(
    query_texts=[question],
    n_results=2
)

print("\nDistances:")
print(results["distances"][0])


# Get retrieved documents
retrieved_chunks = results["documents"][0]

print("\nQuestion:")
print(question)

print("\nRetrieved Chunks:")

for chunk in retrieved_chunks:
    print(chunk)


# Create context from retrieved documents
context = "\n".join(retrieved_chunks)

print("\nContext:")
print(context)


# Create prompt for Gemini
prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""


# Generate final answer
response = gemini_client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)


print("\nFinal Answer:")
print(response.text)