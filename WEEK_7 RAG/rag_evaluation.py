documents = [
    "FastAPI is a Python framework for building APIs.",
    "Python is a programming language.",
    "RAG connects external knowledge with LLMs.",
    "ChromaDB is a vector database used in RAG."
]


# Retrieved chunks
query = "What is FastAPI?"

retrieved_chunks = [
    documents[0],
    documents[2]
]

print("Query:")
print(query)

print("\nRetrieved Chunks:")

for chunk in retrieved_chunks:
    print(chunk)


# Retrieval Precision
relevant_count = 1
retrieved_count = len(retrieved_chunks)

precision = relevant_count / retrieved_count

print("\nRetrieval Precision:")
print(f"{precision:.2f}")


# Retrieval Recall
total_relevant_chunks = 2
retrieved_relevant_chunks = 1

recall = retrieved_relevant_chunks / total_relevant_chunks

print("\nRetrieval Recall:")
print(f"{recall:.2f}")


# F1 Score
f1_score = 2 * (precision * recall) / (precision + recall)

print("\nF1 Score:")
print(f"{f1_score:.2f}")


# Answer Relevance
answer = "FastAPI is a Python framework for building APIs."

if "fastapi" in answer.lower() and "framework" in answer.lower():
    relevance = 1
else:
    relevance = 0

print("\nAnswer Relevance:")
print(relevance)


# Faithfulness
context = "FastAPI is a Python framework for building APIs."

if answer.lower() in context.lower():
    faithfulness = 1
else:
    faithfulness = 0

print("\nFaithfulness:")
print(faithfulness)