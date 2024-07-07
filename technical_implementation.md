# Technical Implementation

This document describes the implementation of the knowledge base.  The knowledge base is deployed is a set of docker containers.  

**Resources**
- [Guide to Setting up Your Local LLM](https://medium.com/@marketing_novita.ai/guide-to-setting-up-your-local-llm-cc45b78413e0)
- [How to create a private ChatGPT that interacts with your local documents](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)
- [Open Source & Self-hosted RAG LLM Server with ChromaDB, Docker & Ollama](https://medium.com/@mbrazel/open-source-self-hosted-rag-llm-server-with-chromadb-docker-ollama-7e6c6913da7a)

# 1. Container: Jupyter Scipy Notebook

The provides a way to run the solution in jupyter.  

**Resources:**

- [Jupyter Docker Stacks](https://github.com/jupyter/docker-stacks)

**Startup:**

- `docker run -it -d -v C:/ML/DU/repos/projects/final/final_project:/home/jovyan/work  -p 8888:8888 quay.io/jupyter/scipy-notebook`


**Access:**

- https://localhost:8888/


# 2. Container: Ollama

**Resources:**

- [Ollama is now available as an official Docker image](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
- [GPU support in Docker Desktop](https://docs.docker.com/desktop/gpu/)
- []()

**Startup:**

`docker run -d --gpus=all -v C:/ML/DU/repos/projects/final/final_project:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

Now you can run a model like Llama 2 inside the container.  **Yes** Run the following command and it will load the model for use by the running container from the previous command.

`docker exec -it ollama ollama run llama3`

Check model:

`/show info`

**Access:**

- http://localhost:11434

** Models:**

More models can be found here:
- [Ollama library](https://ollama.com/library).
- [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file)

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

- **Note** The application code is added to the `streamlit_app.py` file and built into the streamlit docker file.  See the Streamlit [README](README.md) for details.

**Startup:**

`docker run -it -d -p 8501:8501 streamlit`

with local file system:

`docker run -it -d -v /path/to/file/:/app -p 8501:8501 streamlit`

**Access:**

- access the Streamlit app at:  http://localhost:8501
