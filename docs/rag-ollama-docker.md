# RAG, Ollama, in Docker

## Run Ollama Container

**Note:** The ollama Dockerfile is located here: https://github.com/ollama/ollama

### Startup a Container

**CPU Only**

`docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

**Nvidia GPU**

`docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

Run a model

Now you can run a model like Llama 2 inside the container.  **Yes** Run the following command and it will load the model for use by the running container.

`docker exec -it ollama ollama run llama2`

More models can be found here:
- [Ollama library](https://ollama.com/library).
- [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file)


## Run Chroma in a Container

**Note:** The chroma Dockerfile is located here: https://github.com/chroma-core/chroma




# References

- [Ollama is now available as an official Docker image](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
- [Run Chroma DB on a local machine and as a Docker container.](https://abhishektatachar.medium.com/run-chroma-db-on-a-local-machine-and-as-a-docker-container-a9d4b91d2a97)