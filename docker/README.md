# Local Knowledge base with RAG - LLM solution

## Executive Summary

This project implemented a Local Language Model (LLM) capable of reviewing, summarizing, and leveraging proprietary documents.  To do this it uses a Retrieval Augmentation Generation (RAG) workflow.

It runs on a laptop equipped with a 6GB RTX 3060 GPU and 32GB RAM. 

## [The RAG Workflow](../docs/imgs/llamaindex_overview.gif):

- ingests a directory of files as input (Document Repository)
- the files are chunked into smaller docs
- these chunks are embedded and loaded into a vector database.
- **A User can prompt the solution for information**
- the vector database ([chromaDB](chromaDB/README.md)) is queried with the prompt and the #num chucks that most closely match the query are returned.
- These are fed to the LLM model loaded in the LLM server (llama-cpp-python)
- The LLM then provides an answer to the User prompt based on the content of the Document Repository.

The RAG code resides in the `UI-Streamlit` server.

## Installing / Deploying the Solution

The solution is deployed as `3 docker containers`.  This makes it easy to deploy the solution.  You will provide some information about where to find and persist data on your local system.

- `UI-Streamlit` docker container:
  - pass a config file that defines:
    - `Document Respository` directory on local computer or file server.
    - `ChromaDB` server URL
    - `llama-cpp-server` server URL
- `ChromaDB` docker container:
  - pass location to save the database (local directory)
  - pass the embedding model to use.
- `llama-cpp-python` LLM server docker container
  - pass a config file that defines:
    - location of the `LLM model` or models to use
    - provides other server configuration items such as:
      - Authentication (SSL Key and Certificate)
      - Authorization (API-KEY)
      - Port

### Starting up a Docker Container from an Image.




### Running ChromaDB



### Running llama-cpp-python.server


### Running UI_Streamlit

