documents = [
    "FastAPI is a Python framework for building APIs.",
    "FastAPI provides automatic API documentation.",
    "FastAPI supports asynchronous programming.",
    "Python is a programming language.",
    "Machine Learning uses data to train models."
]


# Select Top-K documents
top_k = 3
selected_chunks = documents[:top_k]

print("Selected Context:")

for chunk in selected_chunks:
    print(chunk)


# Limit the context length
max_length = 150
context = ""

for chunk in selected_chunks:
    if len(context) + len(chunk) <= max_length:
        context += chunk + "\n"


print("\nFinal Context:")
print(context)


# Prepare context for the LLM
final_context = context.strip()

print("\nContext for LLM:")
print(final_context)