import numpy as np
from sentence_transformers import SentenceTransformer


documents = [
    "Python is a programming language.",
    "FastAPI is a Python framework for building APIs.",
    "RAG connects external knowledge with LLMs.",
    "ChromaDB is a vector database used in RAG."
]


# Keyword Search
query = "develop APIs"

keyword_results = []

for document in documents:
    if query.lower() in document.lower():
        keyword_results.append(document)


print("Keyword Search Results:")

for document in keyword_results:
    print(document)


# Semantic Search
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

document_embeddings = embedding_model.encode(documents)

query = "FastAPI"
query_embedding = embedding_model.encode(query)

similarities = []

for index, document_embedding in enumerate(document_embeddings):
    similarity = np.dot(
        query_embedding,
        document_embedding
    ) / (
        np.linalg.norm(query_embedding)
        * np.linalg.norm(document_embedding)
    )

    similarities.append((similarity, documents[index]))


similarities.sort(reverse=True)


print("\nSemantic Search Results:")

for score, document in similarities[:2]:
    print(f"Score: {score:.4f}")
    print(document)


# Hybrid Search
hybrid_results = []

for score, document in similarities:
    if document in keyword_results:
        hybrid_score = score + 0.2
    else:
        hybrid_score = score

    hybrid_results.append((hybrid_score, document))


hybrid_results.sort(reverse=True)


print("\nHybrid Search Results:")

for score, document in hybrid_results[:2]:
    print(f"Score: {score:.4f}")
    print(document)