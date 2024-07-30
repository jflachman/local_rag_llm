## Llama-cpp-python TOC
1. [Overview](README.md)
2. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
3. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)
4. [Run the docker image (CUDA or CPU version)](startup-llama-cpp-docker.md)
5. **[Using Llama-cpp server](llama-cpp.md)**
6. [Server Configuration](server_config.md) using a `server.conf` file

---------
---------

# Building a llama-cpp-python server docker image

If you want a smaller image with CPU only support you have two options.

1. Use the stock docker image from llama-cpp-python
2. Use a custom image that can be configured with a `server.config` file

## Option 1: Stock llama-cpp-python docker image

The stock docker image created by the team at [llama-cpp-python](https://github.com/abetlen/llama-cpp-python):

- Pull the latest image:

      docker pull ghcr.io/abetlen/llama-cpp-python:latest

- To pull a specific image such as v0.2.79 use:

      docker pull ghcr.io/abetlen/llama-cpp-python:v0.2.79

- Remember to use the same `tag` of v0.2.79 on the following docker run if you pull that version. 


## Option 2: Llama-cpp-python docker image that can be configured with a `server.config` file

### Unique features of this image:

1. CUDA Support.
2. You may pass and additional argument with a json file with server config settings.  Please see [Starting Llama-cpp.server](starting-llama-cpp.md)

## Build the docker image with server.config support.

- **Prerequisite:** Docker Desktop installed on your computer

Building the image is relatively simple.  From a terminal prompt, enter:

**Generic** 

    docker build -t -f Dockerfile-cpu <a name for your image> .

**Example**

    docker build -t -f Dockerfile-cpu llama-cpp-python:v0.2.83-cpu .

The text after the `:` is the tag.  The image will be called `llama-cpp-python` with a `tag` of `v0.2.83-cpu`.  In this case I use the tag to say it is built using `llama-cpp-python` release `v0.2.83` and it is built with `CPU` support.  But you can name it anything that works for you.

**[!NOTE]**
If you do not need to make further changes to this Dockerfile, then a docker image of this has already be created that can be pulled.

Goto: Docker hub: [jflachman/llama-cpp-python](https://hub.docker.com/repository/docker/jflachman/llama-cpp-python/general)































Create a custom Docker image with CUDA support

The [Dockerfile](docker/Dockerfile-cuda) is used to build a llama-cpp.server docker image with CUDA GPU support.  The current state of the [cuda-simple](https://github.com/abetlen/llama-cpp-python/tree/main/docker/cuda_simple) example from [llama-cpp-python](https://github.com/abetlen/llama-cpp-python/) did not work at the time of this effort.  In addition, after fixing the issues to make it work, the resulting image built with nvidia/cuda-devel image was 13GB.  Additional effort led to a smaller 5GB image.  This is created using the `Dockerfile` in the [docker directory](docker).

### Build the image with CUDA support

- **Prerequisite:** Docker Desktop installed on your computer

Building the image is relatively simple.  From a terminal prompt, enter:

**Generic** 

    docker build -t -f Dockerfile-cuda <a name for your image> .

**Example**

    docker build -t -f Dockerfile-cuda llama-cpp-python:v0.2.77-cuda .

The text after the `:` is the tag.  The image will be called `llama-cpp-python` with a `tag` of `v0.2.77-cuda`.  In this case I use the tag to say it is built using `llama-cpp-python` release `v0.2.77` and it is built with `CUDA` support.  But you can name it anything that works for you.

**[!NOTE]**
If you do not need to make further changes to this Dockerfile, then a docker image of this has already be created that can be pulled.

Goto: Docker hub: [jflachman/llama-cpp-python](https://hub.docker.com/repository/docker/jflachman/llama-cpp-python/general)

### Unique features of this image:

1. CUDA Support.
2. You may pass and additional argument with a json file with server config settings.  Please see [Starting Llama-cpp.server](starting-llama-cpp.md)
   