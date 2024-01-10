import streamlit as st
import os

from llama_index import (
    GPTVectorStoreIndex,
    SimpleDirectoryReader,
    StorageContext,
    load_index_from_storage,
)
persist_dir = "./storage/"

index = None
st.title("Nakka AI")
question = st.text_area("Question")
button = st.button("Ask AI")
st.header("Answer from AI")

def return_response(prompt: str, index):
    query_engine = index.as_query_engine()
    return query_engine.query(prompt).response

if button: 
    with st.spinner('Loading AI model...'):
        # load index
        storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
        index = load_index_from_storage(storage_context)
    with st.spinner('Waiting response from AI ...'):
        answer = return_response(question, index)
    st.write(answer)


