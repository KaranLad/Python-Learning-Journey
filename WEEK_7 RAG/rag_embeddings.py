import os

import chromadb
from dotenv import load_dotenv
from google import genai
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Create embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


# Compare two text embeddings
text1 = "FastAPI is a Python framework for building APIs."
embedding1 = embedding_model.encode(text1)

print("Embedding length:", len(embedding1))


text2 = "FastAPI helps developers create web APIs."
embedding2 = embedding_model.encode(text2)

print("\nSecond embedding length:", len(embedding2))


similarity = cosine_similarity(
    [embedding1],
    [embedding2]
)

print("\nSimilarity:", similarity[0][0])


# Create ChromaDB collection
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="embedding_test"
)

print("\nChromaDB collection created!")


# Add documents and embeddings to ChromaDB
documents = [
    "FastAPI is a Python framework for building APIs.",
    "ChromaDB is a vector database.",
    "Python is a programming language."
]

ids = ["1", "2", "3"]

embeddings = embedding_model.encode(documents).tolist()

collection.add(
    documents=documents,
    embeddings=embeddings,
    ids=ids
)

print("\nDocuments and embeddings added successfully!")


# Create embedding for the user's question
question = input("\nAsk the Question: ")

question_embedding = embedding_model.encode(question).tolist()


# Search for similar documents
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=2
)


print("\nRetrieved Documents:")

for document in results["documents"][0]:
    print(document)


print("\nDistances:")
print(results["distances"][0])


# Create context from retrieved documents
retrieved_chunks = results["documents"][0]

context = "\n".join(retrieved_chunks)

print("\nContext:")
print(context)


# Send context and question to Gemini
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

gemini_client = genai.Client(api_key=api_key)

prompt = f"""
Answer the question using only the context below.

Context:
{context}

Question:
{question}
"""

response = gemini_client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)

print("\nFinal Answer:")
print(response.text)