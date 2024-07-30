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

**Llama-cpp Table of Contents:**
1. llama-cpp-python example:
2. Using Stock Docker Image
3. Create a custom Docker image with CUDA support
4. Run the docker image with CUDA support
5. **Using Llama-cpp server**
6. Server Configuration using a `server.conf` file
7. Encryption & Authentication
8. References



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

Note:  Local path to models for docker on WSL used in the examples a windows directory:  `C:/ML/DU/local_rag_llm/models`.  Also, `/home/user/rag_llm` is a softlink to `/mnt/c/ML/CU/local_rag_llm`

## 1. llama-cpp-python example:

Ran example from sunny2309: [Llama CPP Turorial](llama-cpp-tutorial.ipynb)

- Ran perfectly with modifications for local llm `/home/user/rag_llm/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf`.  made this a variable llm_model.

## 2. Using Stock Docker Image

Tried out the docker image created by the team at [llama-cpp-python](https://github.com/abetlen/llama-cpp-python):

- Pull the latest image:

      docker pull ghcr.io/abetlen/llama-cpp-python:latest

- To pull a specific image such as v0.2.79 use:

      docker pull ghcr.io/abetlen/llama-cpp-python:v0.2.79

- Remember to use the same `tag` of v0.2.79 on the following docker run if you pull that version. 

- **generic**

      docker run --rm -it -d -p 8000:8000 -v /path/to/models:/models -e MODEL=/models/llama-model.gguf ghcr.io/abetlen/llama-cpp-python:latest

- **My parameters**

      docker run -it -p 8100:8000 -v C:/ML/DU/local_rag_llm/models:/models -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf  ghcr.io/abetlen/llama-cpp-python:latest

- **Your parameters:**

  - Try the my parameters version above, but modify `C:/ML/DU/local_rag_llm/models` to the location of the database on you local directory.  You may also have a different Model downloaded.  So enter the path to that model from your local directory.
    - Therefore, if you model is in `C:/ML/DU/local_rag_llm/models/qwen2_500m` and the model name is `qwen2-0_5b-instruct-q5_k_m.gguf`, then use:  `-e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf`


## 3. Create a custom Docker image with CUDA support

The [Dockerfile](docker/Dockerfile) is used to build a llama-cpp.server docker image with CUDA GPU support.  The current state of the [cuda-simple](https://github.com/abetlen/llama-cpp-python/tree/main/docker/cuda_simple) example from [llama-cpp-python](https://github.com/abetlen/llama-cpp-python/) did not work at the time of this effort.  In addition, after fixing the issues to make it work, the resulting image built with nvidia/cuda-devel image was 13GB.  Additional effort led to a smaller 5GB image.  This is created using the `Dockerfile` in the [docker directory](docker).

### Build the image with CUDA support

- **Prerequisite:** Docker Desktop installed on your computer

Building the image is relatively simple.  From a terminal prompt, enter:

**Generic** 

    docker build -t <a name for your image> .

**Example**

    docker build -t llama-cpp-python:2.77-cuda .

The text after the `:` is the tag.  The image will be called `llama-cpp-python` with a `tag` of `2.77-cuda`.  In this case I use the tag to say it is built using `llama-cpp-python` release `2.77` and it is built with `CUDA` support.  But you can name it anything that works for you.

## 4. Run the docker image with CUDA support

**Generic**

    docker run -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model name> -v <local direcctory on host>:/var/model <image name>

**Example**

    docker run -it -d -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python:2.77-cuda

**Flags:**  There are several docker flags to set when starting the llama-cpp-python server.

- `-v` Bind mount a volume.  I our case it mounts local directory `C:/ML/local_rag_llm/models` to container directory `/var/model`  Note that llama-cpp will look for models in /var/model
- `-p` Publish a container's port(s) to the host.  In our case it exposes container port `8000` to localhost port `8100`
- `-d` Run container in background and print container ID or in other words it runs container disconnected (returns to terminal prompt)
- `--name` Assign a name to the container.  when omitted docker assigns a random name
- `-e` Set environment variables
- `-gpus=all` GPU devices to add to the container ('all' to pass all GPUs)
- `--cap-add` Add Linux capabilities
- `i` Keep STDIN open even if not attached
- `t` Allocate a pseudo-TTY

### 4.1.  ALTERNATE: Run the CUDA docker image with an environment file

You can also create a `.llama_cpp_env` file setting the required environment variables and pass it to the Docker container with the `--env-file` flag when running the container.  This can simplify your `docker run` command

- **.llama_cpp_env** file contents (filename is arbitrary)

        USE_MLOCK=0
        MODEL=/var/model/<model-path>/<model_file>

- using .llama_cpp_file
  
      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE --env-file ./.llama_cpp_env -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python-cuda


## 5. Using Llama-cpp server.

Once your server is running, you may access it here:  http://localhost:8100/docs

**References**

- https://llama-cpp-python.readthedocs.io/en/latest/
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)






## 6. Server Configuration using a `server.config` file

The CUDA enabled docker container from `Section 3: Create a custom Docker image with CUDA support` is built to allow an server.conf file to be passed when starting up the container.  A good place to put this file is in the `/var/models` directory.  See the default [server.config](../../../../models/server.config) file there.  The file name is arbitrary.  So you could use `best_models.conf` for example.

    run -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v C:/ML/DU/local_rag_llm/models:/var/model  jflachman/llama-cpp-python:v0.2.77-cuda /var/model/server.config

For more information on parameters for configuring the server see:

- [Server Options Reference](https://llama-cpp-python.readthedocs.io/en/latest/server/#server-options-reference)
- [Configuration and Multi-Model Support](https://llama-cpp-python.readthedocs.io/en/latest/server/#configuration-and-multi-model-support) - has a sample `server.config` and show how to configure/load multiple models.
- https://llama-cpp-python.readthedocs.io/en/latest/server/


### 7. Encryption & Authentication

**Encryption** is accomplished by setting the `ssl_keyfile` and the `ssl_certificate`.  There are many ways to generate these.  A google search should provide some.

**Authentication** can be accomplished with an `API_KEY`.  All authentication requests use this key.  This is typically a secret shared between the UI application and the LLM server.


**References**
- https://llama-cpp-python.readthedocs.io/en/latest/server/#llama_cpp.server.settings.ServerSettings

**Server settings** used to configure the FastAPI and Uvicorn server:

- `host`: str = Field(default="localhost", description="Listen address")
- `port`: int = Field(default=8000, description="Listen port")
- `ssl_keyfile`: SSL key file for HTTPS
- `ssl_certfile`: SSL certificate file for HTTPS
- `api_key`: API key for authentication. If set all requests need to be authenticated.
- `interrupt_requests`: Whether to interrupt requests when a new request is received.
- `disable_ping_events`: Disable EventSource pings (may be needed for some clients).
- `root_path`: The root path for the server. Useful when running behind a reverse proxy.




## 8. References

- https://llama-cpp-python.readthedocs.io/en/latest/
- https://github.com/abetlen/llama-cpp-python
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)


### 8.1 Typical Model Sizes


| Model |  Quantized size |
|------:|----------------:|
|    3B |            3 GB |
|    7B |            5 GB |
|   13B |           10 GB |
|   33B |           25 GB |
|   65B |           50 GB |
