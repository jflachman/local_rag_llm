# Local Knowledge base deployment

This solution uses docker deployments of some of the components.


## 1. Container: Jupyter Notebook, 

The provides a way to run the solution in jupyter.  

start container

`docker run -it -d -v C:/ML/DU/repos/projects/final/final_project:/home/jovyan/work  -p 8888:8888 quay.io/jupyter/scipy-notebook`


## 2. Container: Ollama

start the container

`docker run -d --gpus=all -v C:/ML/DU/repos/projects/final/final_project:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

Now you can run a model like Llama 2 inside the container.  **Yes** Run the following command and it will load the model for use by the running container from the previous command.

`docker exec -it ollama ollama run llama3`

Check model:

`/show info`

## 3. Container: ChromaDB

See: 
- https://medium.com/@pierrelouislet/getting-started-with-chroma-db-a-beginners-tutorial-6efa32300902
- https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide
- Docker: https://docs.trychroma.com/deployment/aws#docker


**Start Chroma Server**

    `docker pull chromadb/chroma`

    `docker run -it -d -v /path/to/local/db/:/chroma/chroma -p 8000:8000 chromadb/chroma`

    <or>

    docker run --env-file ./.chroma_env -p 8000:8000 chromadb/chroma


**Create Chroma Client**

    ```
    import chromadb
    chroma_client = chromadb.HttpClient(host='localhost', port=8000)
    ```

- See step-by-step guide for info on persistent DB.

## 4. Container: Streamlit & Application

`docker run -it -d -p 8501:8501 streamlit`

with local file system:

`docker run -it -d -v /path/to/file/:/app -p 8501:8501 streamlit`

