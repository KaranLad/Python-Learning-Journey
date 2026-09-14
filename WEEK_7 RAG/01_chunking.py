from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
FastAPI is a Python framework for building APIs.

It is fast and easy to use.

ChromaDB is a vector database.

It stores and searches vector embeddings.
"""


splitter = RecursiveCharacterTextSplitter(
    chunk_size=50,
    chunk_overlap=10
)

chunks = splitter.split_text(text)


for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}:")
    print(chunk)