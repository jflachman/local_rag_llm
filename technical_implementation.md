## Table of Contents

 - [README](README.md)
 - [Project Proposal](docs/project_proposal.md)
 - [Technical Approach](docs/technical_approach.md)
 - [Technical Implementation](technical_implementation.md)
 - [Prototypes](Prototypes/README.md) developed in support of the Technical Approach & Implementation
 - Research, Trades and References
   - [Knowledge Documents](docs/knowledge_documents.md)
   - [User Interface](docs/user_interface.md)
   - [LLMs](docs/LLMs.md)
   - [Embeddings](docs/embedding.md)
   - [Vector Database](docs/vectorDB.md)
   - [Other Notes](docs/misc_notes.md)
   - [References](docs/references.md)

# Technical Implementation

This document describes the implementation of the knowledge base.  The knowledge base is deployed is a set of docker containers.  

**Resources**
- [Guide to Setting up Your Local LLM](https://medium.com/@marketing_novita.ai/guide-to-setting-up-your-local-llm-cc45b78413e0)
- [How to create a private ChatGPT that interacts with your local documents](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)
- [Open Source & Self-hosted RAG LLM Server with ChromaDB, Docker & Ollama](https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a)

# 1. Container: Jupyter Scipy Notebook 

This container is not required for this project.  It provides an easily deployable Python/Jupyter environment if needed/desired and provides a way to prototype and test in jupyter if desired.  Additional packages may be installed in the container through the exec tab in docker desktop.  Using a requirements.txt file accessible through `/home/jovyan/work` in the container allows for bulk installation of packages.  See notes on [WSL/Jupyter environment with VSCode](https://github.com/jflachman/class-notes/blob/main/1.2.3_tool_setup_docker.md) for more information

**Resources:**

- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)

**Startup:**

- `docker run -it -d -v C:/ML/DU/repos/projects/final/local_rag_llm:/home/jovyan/work  -p 8888:8888 quay.io/jupyter/scipy-notebook`


**Access:**

- https://localhost:8888/


# 2. Container: llama-cpp-server

See the [LLM-server](../prototype/jeff/2-llm-server/README.md) prototype for details:

**Resources:**

- https://llama-cpp-python.readthedocs.io/en/latest/
- https://github.com/abetlen/llama-cpp-python
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)

**Startup:**

-   *Generic*

        docker run --rm -it -p 8000:8000 -v /path/to/models:/models -e MODEL=/models/llama-model.gguf ghcr.io/abetlen/llama-cpp-python:latest

-   *My parameters*

        docker run -it -p 8100:8000 -v C:/ML/DU/local_rag_llm/models:/models -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf  ghcr.io/abetlen/llama-cpp-python:latest

**Check model:**

- http://localhost:8100/v1/models

**Check GPU Support**



**Access:**

- http://localhost:8100

** Models:**

See:  https://huggingface.co

# 3. Container: ChromaDB

**Resources:**
- https://docs.trychroma.com/deployment/aws#docker
- https://medium.com/@pierrelouislet/getting-started-with-chroma-db-a-beginners-tutorial-6efa32300902
- https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide
- Docker: https://docs.trychroma.com/deployment/aws#docker
- [Open Source & Self-hosted RAG LLM Server with ChromaDB, Docker & Ollama](https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a)
- [Run Chroma DB on a local machine and as a Docker container.](https://abhishektatachar.medium.com/run-chroma-db-on-a-local-machine-and-as-a-docker-container-a9d4b91d2a97)

**Startup:**

- **Start Chroma Server**

    `docker pull chromadb/chroma`

    `docker run -it -d -v /path/to/local/db/:/chroma/chroma -p 8000:8000 chromadb/chroma`

    <or>

    docker run --env-file ./.chroma_env -p 8000:8000 chromadb/chroma

- **Create Chroma Client**

    ```
    import chromadb
    chroma_client = chromadb.HttpClient(host='localhost', port=8000)
    ```

- See step-by-step guide for info on persistent DB.

**Access:**

- http://localhost:8000


# 4. Container: Streamlit

**Resources:**
- https://docs.streamlit.io/deploy/tutorials/docker
- https://github.com/streamlit/streamlit-example
- https://medium.com/@stefnestor/python-streamlit-local-llm-2aaa75961d03

**Build the Container**

`docker build -t streamlit .`

- **Note** The application code is added to the `streamlit_app.py` file and built into the streamlit docker file.  See the Streamlit [README](README.md) for details.

**Startup:**

`docker run -it -d -p 8501:8501 streamlit`

with local file system:

`docker run -it -d -v /path/to/file/:/app -p 8501:8501 streamlit`

**Access:**

- access the Streamlit app at:  http://localhost:8501


# Application