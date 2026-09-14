question = "What is FastAPI?"


retrieved_chunks = [
    "FastAPI is a Python framework used to build APIs.",
    "FastAPI provides automatic API documentation.",
    "ChromaDB is a vector database.",
    "Machine Learning uses data to train models.",
    "FastAPI supports asynchronous programming."
]


print("Question:")
print(question)


print("\nRetrieved Context:")

for chunk in retrieved_chunks:
    print("-", chunk)


# Filter relevant chunks
relevant_chunks = []

for chunk in retrieved_chunks:
    if "FastAPI" in chunk:
        relevant_chunks.append(chunk)


print("\nFiltered Context:")

for chunk in relevant_chunks:
    print("-", chunk)


print("\nTotal Relevant Chunks:")
print(len(relevant_chunks))