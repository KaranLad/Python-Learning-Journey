from sentence_transformers import CrossEncoder


# Load Cross-Encoder model
reranker = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


documents = [
    "Python is a programming language.",
    "FastAPI is a Python framework for building APIs.",
    "RAG connects external knowledge with LLMs.",
    "Python has lists, tuples and dictionaries.",
    "Machine Learning uses data to train models."
]


query = "How can I build APIs using Python?"


# Initial retrieval results
results = [
    (0.72, documents[0]),
    (0.68, documents[1]),
    (0.61, documents[2]),
    (0.59, documents[3]),
    (0.55, documents[4])
]


print("Retrieved Results:")

for score, document in results:
    print(f"{score:.2f} - {document}")


# Simple rule-based reranking
reranked_results = []

for score, document in results:
    if "api" in document.lower() or "apis" in document.lower():
        score += 0.20

    reranked_results.append((score, document))


reranked_results.sort(reverse=True)


print("\nRule-Based Reranked Results:")

for score, document in reranked_results[:3]:
    print(f"{score:.2f} - {document}")


# Cross-Encoder reranking
pairs = []

for _, document in results:
    pairs.append([query, document])


reranker_scores = reranker.predict(pairs)


print("\nCross-Encoder Scores:")

for document, score in zip(
    [document for _, document in results],
    reranker_scores
):
    print(f"{score:.4f} - {document}")


# Sort documents using Cross-Encoder scores
final_results = list(
    zip(
        reranker_scores,
        [document for _, document in results]
    )
)

final_results.sort(reverse=True)


print("\nFinal Reranked Results:")

for score, document in final_results:
    print(f"{score:.4f} - {document}")