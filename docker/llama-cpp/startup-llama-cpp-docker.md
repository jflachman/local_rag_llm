## Llama-cpp-python TOC
1. [Overview](README.md)
2. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
3. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)
4. [Run the docker image (CUDA or CPU version)](startup-llama-cpp-docker.md)
5. **[Using Llama-cpp server](llama-cpp.md)**
6. [Server Configuration](server_config.md) using a `server.conf` file

---------
---------

# Startup Llama-cpp-python server

## Run the server

The server is pre-built in a docker image.  There is no code to install or compile.  Simply run the docker image.  There are two options:

1. docker image that uses you CPU
2. docker image that can use your GPU

Configuration Options:

3. Docker run `flags`
4. add [server.config](server_config.md) to the startup

## 1. Run the docker image for CPU only

**Generic**

    docker run -it -d -p 8000:8000 --gpus=all -e MODEL=/var/model/<model name> -v <local direcctory on host>:/var/model <image name>

**Example**

    docker run -it -d -p 8100:8000 --gpus=all -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v C:/ML/DU/local_rag_llm/models:/var/model jflachman/llama-cpp-python:v0.2.83-cpu

## 2. Run the docker image with Nvidia GPU (CUDA) support

**Generic**

    docker run -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model name> -v <local direcctory on host>:/var/model <image name>

**Example**

    docker run -it -d -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v C:/ML/DU/local_rag_llm/models:/var/model jflachman/llama-cpp-python:v0.2.77-cuda

### 2.1.  ALTERNATE: Run the CUDA docker image with an environment file

You can also create a `.llama_cpp_env` file setting the required environment variables and pass it to the Docker container with the `--env-file` flag when running the container.  This can simplify your `docker run` command

- **.llama_cpp_env** file contents (filename is arbitrary)

        USE_MLOCK=0
        MODEL=/var/model/<model-path>/<model_file>

- using .llama_cpp_file
  
      docker run  --rm -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE --env-file ./.llama_cpp_env -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python-cuda


## 3. Docker Run Flags

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

### GPU / CUDA specific flags

- `--cap-add SYS_RESOURCE` 	Override resource Limits
- `-e USE_MLOCK=0` USE_MLOCK=True decrease model load time to almost zero (as it is already in mem)
- `-gpus=all` GPU devices to add to the container ('all' to pass all 

## 4. Add Server Config (server.config)

