**Prototypes Table of Contents**

0. [Prototypes Overview](../../README.md)
1. [Build AIML python environment](../../1-build-env/README.md)
2. [LLM Server](../2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
   1. [Llama-cpp-python](../llama-cpp/README.md)
   2. [Ollama](../ollama/README.md)3. [Vector Database](../../3-vectorDB/README.md)
3. [Vector Database](../../3-vectorDB/README.md)
4. [User Interface](../../4-user-interface/README.md)
5. TBD - [RAG Workflow](../../5-rag-workflow/README.md)
6. TBD - [RAG & UI integration](../../6-rag-ui-integration/README.md)

---------
---------

# LLM Server Investigation - llama-cpp-python

## **Summary**
The goal was to deploy of CUDA docker version of Llama-cpp-python.  However, some issues that "appear" to be in my docker environment and nuances of llama-cpp-python prevented creating a cuda enabled docker container.  I am working in the llama-cpp-python discussion section on github to find a resolution.

Therefore, the rest fo this discussion is halted mid-development until the CUDA docker solution is resolved.

## Overview  

**Objective:** host an OpenAI compliant server in docker running a local LLM model from Huggingface.

Steps:
1. Run llama-cpp-python examples in Jupyter
2. Run a stock docker container
    - Determine if this container satisfies step 3.
3. Build a docker container with:
    - CUDA GPU support
    - OpenAI compliant API

**Step 3 is TBD**

Note:  Local path to models for docker on WSL is:  `C:/ML/DU/local_rag_llm/models`.  Also, `/home/user/rag_llm` is a softlink to `/mnt/c/ML/CU/local_rag_llm`

## 1. llama-cpp-python example:

Ran example from sunny2309: [Llama CPP Turorial](llama-cpp-tutorial.ipynb)

- Ran perfectly with modifications for local llm `/home/user/rag_llm/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf`.  made this a variable llm_model.

## 2. Stock Docker Container

Tried out available docker image:

- **generic**

      docker run --rm -it -d -p 8000:8000 -v /path/to/models:/models -e MODEL=/models/llama-model.gguf ghcr.io/abetlen/llama-cpp-python:latest

- **My parameters**

      docker run -it -p 8100:8000 -v C:/ML/DU/local_rag_llm/models:/models -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf  ghcr.io/abetlen/llama-cpp-python:latest

- **Your parameters:**

  - Try the my parameters version above, but modify `C:/ML/DU/local_rag_llm/db` to the location of the database on you local directory.

## 3. Create a custom image with CUDA support

A simple [docker file](https://github.com/abetlen/llama-cpp-python/tree/main/docker/cuda_simple) is available from llama-cpp-python.  This is the source of the Dockerfile included in this investigation.

This dockerfile uses a base linux image with CUDA already installed from Nvidia with these lines in the DOckerfile:

    ARG CUDA_IMAGE="12.5.0-devel-ubuntu22.04"
    FROM nvidia/cuda:${CUDA_IMAGE}

**Note:**  The stock [Dockerfile](https://github.com/abetlen/llama-cpp-python/tree/main/docker/cuda_simple) was modified to use the following llama-cpp-python pip install.  Without this update to point to the whl file, the build failed.  The Nvidia CUDA base image uses CUDA 12.5 while the whl file uses 12.4 (the latest whl currently available: cu124).  CUDA is backward compatible, so llama-cpp-python with 12.4 support will work with CUDA 12.5.

    RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install --no-cache-dir llama-cpp-python==0.2.79 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124

After making this one change, the Dockerfile build completed successfully


### 3a. Build the image with CUDA support

To build the docker image with cuda support.

1. Navigate to this directory `2-llm-server`
2. run:

        docker build -t llama-cpp-python-cuda .

### 3b. Startup a container with the new image

- **Generic**

      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model-path> -v <model-root-path>:/var/model llama-cpp-python-cuda

- **My Parameters**

      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python-cuda

### 3b.1.  Startup with an environment file

You can also create a `.llama_cpp_env` file setting the required environment variables and pass it to the Docker container with the `--env-file` flag when running the container.  This will be useful when adding authentication.

- **Generic**

      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model-path> -v <model-root-path>:/var/model llama-cpp-python-cuda

- **My Parameters**

      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE --env-file ./.llama_cpp_env -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python-cuda

Note:  `--cap-add SYS_RESOURCE` Overrides resource Limits.


- **.llama_cpp_env** file contents (filename is arbitrary)

        USE_MLOCK=0
        MODEL=/var/model/<model-path>

### 4. Authentication

**References**
- See Authentication in https://github.com/abetlen/llama-cpp-python/blob/main/llama_cpp/server/settings.py
- See Changelog 0.2.25: https://github.com/abetlen/llama-cpp-python/blob/main/CHANGELOG.md

Server settings used to configure the FastAPI and Uvicorn server:

- `host`: str = Field(default="localhost", description="Listen address")
- `port`: int = Field(default=8000, description="Listen port")
- `ssl_keyfile`: SSL key file for HTTPS
- `ssl_certfile`: SSL certificate file for HTTPS
- `api_key`: API key for authentication. If set all requests need to be authenticated.
- `interrupt_requests`: Whether to interrupt requests when a new request is received.
- `disable_ping_events`: Disable EventSource pings (may be needed for some clients).
- `root_path`: The root path for the server. Useful when running behind a reverse proxy.




### 3c. Test

-   Verify GPU support

        from llama_cpp import Llama
        llm = Llama(model_path="./llama-2-7b/ggml-model-f16.gguf", n_gpu_layers=-1)

**TBD**



## 4. References

- https://llama-cpp-python.readthedocs.io/en/latest/
- https://github.com/abetlen/llama-cpp-python
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)
