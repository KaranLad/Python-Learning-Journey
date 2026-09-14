import chromadb


chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="metadata_collection"
)


documents = [
    "Python is a programming language.",
    "FastAPI is a Python framework for building APIs.",
    "RAG is used to connect external knowledge with LLMs."
]


metadatas = [
    {"topic": "Python", "source": "python.pdf"},
    {"topic": "FastAPI", "source": "fastapi.pdf"},
    {"topic": "RAG", "source": "rag.pdf"}
]


ids = ["1", "2", "3"]


# Store documents with metadata
collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("Documents and metadata stored successfully!")


# Filter documents using metadata
results = collection.get(
    where={"topic": "Python"}
)

print("\nFiltered Documents:")

for document in results["documents"]:
    print(document)


# Metadata filtering with similarity search
results = collection.query(
    query_texts=["How can I build an API with Python?"],
    n_results=2,
    where={
        "$or": [
            {"topic": "Python"},
            {"topic": "RAG"}
        ]
    }
)


print("\nFiltered Search Results:")

for document in results["documents"][0]:
    print(document)