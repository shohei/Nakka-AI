import os

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)

persist_dir = "./storage/"

# load from disk
storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
# load index
index = load_index_from_storage(storage_context)

def print_response(prompt: str, index):
    query_engine = index.as_query_engine()
    print(query_engine.query(prompt))

while True:
    user_input = input("[Type your question]: ")
    print()
    print_response(user_input, index)
    print()
