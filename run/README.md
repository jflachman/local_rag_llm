# Local Knowledge base with RAG - LLM solution

## 1. Executive Summary

This project implemented a Local Language Model (LLM) capable of reviewing, summarizing, and leveraging proprietary documents.  To do this it uses a Retrieval Augmentation Generation (RAG) workflow.

It runs on a laptop equipped with a 6GB RTX 3060 GPU and 32GB RAM. 

## 2. Run the RAG

The RAG Solution is implemented in two docker containers and two jupyter notebooks.

- To startup the Docker containers, see the [README in docker](../docker/README.md)
- To read and load the database, run the [01_load_docs_vectordb.ipnyb](01_load_docs_vectordb.ipnyb) file
- To Query the RAG system run the [02_rag_query.ipynb](02_rag_query.ipynb) file

In the next phase, the codes in these `jupyter notebooks` will be added to a `docker image` with a Streamlit or Gradio User Interface.


