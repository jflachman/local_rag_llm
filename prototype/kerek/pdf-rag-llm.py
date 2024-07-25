import streamlit as st
import os

from langchain_groq import ChatGroq
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

from langchain_core.prompts import ChatPromptTemplate


## Groq api key
groq_api_key = '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'

st.title("GROQ with Llama3")

llm = ChatGroq(groq_api_key = groq_api_key,
               model_name = "Llama3-8b-8192")


prompt=ChatPromptTemplate.from_template(
"""
Answer the questions based on the provided context only.
Please provide the most accurate response based on the question
<context>
{context}
<context>
Questions:{input}

"""
)

def vector_embedding():

    if "vectors" not in st.session_state:    
        st.session_state.embeddings = OllamaEmbeddings()
        st.session_state.loader = PyPDFLoader("Traditional System of Medicine.pdf")
        st.session_state.docs = st.session_state.loader.load()
        st.session_state.final_documents = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200).split_documents(st.session_state.docs[:10])
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents,st.session_state.embeddings)  


prompt1=st.text_input("Input your question here")


if st.button("Documents Embedding"):
    vector_embedding()
    st.write("Vector DB is ready")

import time

if prompt1:
    start = time.process_time()
    document_chain = create_stuff_documents_chain(llm,prompt) 
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever,document_chain)
    response = retrieval_chain.invoke({'input':prompt1})

    print("Response Time :" ,time.process_time()-start)
    st.write(response['answer'])

   # With a streamlit expander
    with st.expander("Document Similarity Search"):
        # Find the relevant chunks
        for i, doc in enumerate(response["context"]):
            st.write(doc.page_content)
            st.write("--------------------------------")