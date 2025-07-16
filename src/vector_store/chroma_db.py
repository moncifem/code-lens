from langchain_chroma import Chroma
from typing import Callable

vector_store = None

def get_vector_store(collection_name: str, embedding_function: Callable):
    global vector_store
    if vector_store is None:
        vector_store = Chroma(
        collection_name=collection_name,
        embedding_function=embedding_function,
        persist_directory="./chroma_db"
        )
    return vector_store

