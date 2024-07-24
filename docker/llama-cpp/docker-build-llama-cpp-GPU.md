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

Create a custom Docker image with CUDA support

The [Dockerfile](docker/Dockerfile-cuda) is used to build a llama-cpp.server docker image with CUDA GPU support.  The current state of the [cuda-simple](https://github.com/abetlen/llama-cpp-python/tree/main/docker/cuda_simple) example from [llama-cpp-python](https://github.com/abetlen/llama-cpp-python/) did not work at the time of this effort.  In addition, after fixing the issues to make it work, the resulting image built with nvidia/cuda-devel image was 13GB.  Additional effort led to a smaller 5GB image.  This is created using `Dockerfile-cuda`.

See my post concerning the results of this effort on the llama-cpp-python discussion here: [Building Dockerfile with CUDA support and smaller image](https://github.com/abetlen/llama-cpp-python/discussions/1609)

The resulting Dockerfile builds in two stages.

This will build in two stages
1. **Stage 1:** The CUDA 'devel' base image will be used to build llama-cpp-python with CUDA support (~13GB image) This used the base image: `nvidia/cuda:12.1.1-devel-ubuntu22.04`
2. **Stage 2:** The CUDA 'runtime' base image will then be used and the llama-cpp build from the devel image will be copied to the new runtime image (5GB final image)  This used the base image: `nvidia/cuda:12.1.1-runtime-ubuntu22.04`

See the final [Dockerfile](Dockerfile) for more information

## Build the image with CUDA support

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
   

## [!NOTE] an alternate to llama-cpp-python is the base llama-cpp in docker

However, this is not covered in this project.

- https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md