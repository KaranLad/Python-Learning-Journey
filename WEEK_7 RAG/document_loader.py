import os

import chromadb
from dotenv import load_dotenv
from google import genai
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer


# Load PDF
reader = PdfReader("knowledge.pdf")

pdf_text = ""

for page in reader.pages:
    text = page.extract_text()

    if text:
        pdf_text += text


# Split PDF text into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

chunks = splitter.split_text(pdf_text)

print("\nTotal Chunks:", len(chunks))

for index, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {index} ---")
    print(chunk)


# Create embeddings for each chunk
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = embedding_model.encode(chunks)

print("\nNumber of Embeddings:", len(embeddings))
print("Embedding Dimensions:", len(embeddings[0]))


# Store chunks and embeddings in ChromaDB
chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="pdf_collection"
)

ids = [str(index) for index in range(len(chunks))]
embeddings_list = embeddings.tolist()

collection.add(
    documents=chunks,
    embeddings=embeddings_list,
    ids=ids
)

print("\nPDF chunks and embeddings stored in ChromaDB!")


# Get question from the user
question = input("\nAsk your question: ")

question_embedding = embedding_model.encode(question).tolist()

print("\nQuestion embedding created!")
print("Embedding dimensions:", len(question_embedding))


# Search ChromaDB for relevant chunks
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

retrieved_chunks = results["documents"][0]

print("\nRetrieved Chunks:")

for index, chunk in enumerate(retrieved_chunks, start=1):
    print(f"\n--- Result {index} ---")
    print(chunk)

print("\nDistances:")
print(results["distances"][0])


# Create context for the LLM
context = "\n".join(retrieved_chunks)

print("\nContext:")
print(context)


# Generate answer using Gemini
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