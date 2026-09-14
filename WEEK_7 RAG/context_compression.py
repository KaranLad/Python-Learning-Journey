import numpy as np
from sentence_transformers import SentenceTransformer


documents = [
    "FastAPI is a Python framework for building APIs.",
    "FastAPI provides automatic API documentation.",
    "Python is a programming language.",
    "Machine Learning uses data to train models."
]

query = "FastAPI APIs"


# Keyword-based filtering
relevant_chunks = []

for document in documents:
    if "fastapi" in document.lower() or "api" in document.lower():
        relevant_chunks.append(document)


print("Keyword-Based Context:")

for chunk in relevant_chunks:
    print(chunk)


# Semantic similarity
model = SentenceTransformer("all-MiniLM-L6-v2")

query_embedding = model.encode(query)

scored_chunks = []

for document in documents:
    document_embedding = model.encode(document)

    similarity = np.dot(query_embedding, document_embedding) / (
        np.linalg.norm(query_embedding)
        * np.linalg.norm(document_embedding)
    )

    scored_chunks.append((similarity, document))


scored_chunks.sort(reverse=True)


print("\nSemantic Relevance:")

for score, document in scored_chunks:
    print(f"{score:.4f} - {document}")


# Keep only relevant documents
threshold = 0.50
compressed_context = []

for score, document in scored_chunks:
    if score >= threshold:
        compressed_context.append(document)


print("\nCompressed Context:")

for document in compressed_context:
    print(document)