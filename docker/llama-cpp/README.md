# Llama-cpp-python Docker Image

This discussion and files are from:

- [Llama-cpp-python](https://github.com/abetlen/llama-cpp-python/docker)
- https://github.com/abetlen/llama-cpp-python/issues/1119
- https://hub.docker.com/r/nvidia/cuda/

## Build an image with for CPU only

    docker build -t llama-cpp-python:v0.2.82 -f Dockerfile-cpu .

Run Container:

**Generic**

    docker run -it -d -p 8000:8000 -e MODEL=/var/model/<model name> -v <local direcctory on host>:/var/model <image name>

**Example**

    docker run -it -d -p 8100:8000 -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v C:/ML/DU/local_rag_llm/models:/var/model llama-cpp-python:v0.2.82-cpu


## Build an image with CUDA GPU support

### Create a Dockerfile to build the image.

The Dockerfile is used to build a llama-cpp.server docker image with CUDA GPU support.  The current state of the cuda-simple example in the References below did not work at the time of this effort.  In addition, after fixing the issues, the resulting image built with nvidia/cuda-devel image was 13GB.  Additional effort led to a smaller 5GB image.

See my post concerning the results of this effort on the llama-cpp-python discussion here: [Building Dockerfile with CUDA support and smaller image](https://github.com/abetlen/llama-cpp-python/discussions/1609)

The resulting Dockerfile builds in two stages.

This will build in two stages
1. **Stage 1:** The CUDA 'devel' base image will be used to build llama-cpp-python with CUDA support (~13GB image) This used the base image: `nvidia/cuda:12.1.1-devel-ubuntu22.04`
2. **Stage 2:** The CUDA 'runtime' base image will then be used and the llama-cpp build from the devel image will be copied to the new runtime image (5GB final image)  This used the base image: `nvidia/cuda:12.1.1-runtime-ubuntu22.04`

See the final [Dockerfile](Dockerfile) for more information

### Build the Docker Image with CUDA support

- **Prerequisite:** Docker Desktop installed on your computer

Building the image is relatively simple.  From a terminal prompt, enter:

**Generic** 

    docker build -t <a name for your image> .

**Example**

    docker build -t llama-cpp-python:2.77-cuda .

The text after the `:` is the tag.  The image will be called `llama-cpp-python` with a `tag` of `2.77-cuda`.  In this case I use the tag to say it is built using `llama-cpp-python` release `2.77` and it is built with `CUDA` support.  But you can name it anything that works for you.

## Run the docker image

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

# References

## Simple Dockerfiles for building the llama-cpp-python server with external model bin files
### openblas_simple
A simple Dockerfile for non-GPU OpenBLAS, where the model is located outside the Docker image:
```
cd ./openblas_simple
docker build -t openblas_simple .
docker run --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model-path> -v <model-root-path>:/var/model -t openblas_simple
```
where `<model-root-path>/<model-path>` is the full path to the model file on the Docker host system.

### cuda_simple
> [!WARNING]  
> Nvidia GPU CuBLAS support requires an Nvidia GPU with sufficient VRAM (approximately as much as the size in the table below) and Docker Nvidia support (see [container-toolkit/install-guide](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html)) <br>

A simple Dockerfile for CUDA-accelerated CuBLAS, where the model is located outside the Docker image:

```
cd ./cuda_simple
docker build -t cuda_simple .
docker run --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/<model-path> -v <model-root-path>:/var/model -t cuda_simple
```
where `<model-root-path>/<model-path>` is the full path to the model file on the Docker host system.

--------------------------------------------------------------------------

### "Open-Llama-in-a-box"
Download an Apache V2.0 licensed 3B params Open LLaMA model and install into a Docker image that runs an OpenBLAS-enabled llama-cpp-python server:
```
$ cd ./open_llama
./build.sh
./start.sh
```

### Manually choose your own Llama model from Hugging Face
`python3 ./hug_model.py -a TheBloke -t llama`
You should now have a model in the current directory and `model.bin` symlinked to it for the subsequent Docker build and copy step. e.g.
```
docker $ ls -lh *.bin
-rw-rw-r-- 1 user user 4.8G May 23 18:30 <downloaded-model-file>q5_1.bin
lrwxrwxrwx 1 user user   24 May 23 18:30 model.bin -> <downloaded-model-file>q5_1.bin
```

> [!NOTE]  
> Make sure you have enough disk space to download the model. As the model is then copied into the image you will need at least
**TWICE** as much disk space as the size of the model:<br>

| Model |  Quantized size |
|------:|----------------:|
|    3B |            3 GB |
|    7B |            5 GB |
|   13B |           10 GB |
|   33B |           25 GB |
|   65B |           50 GB |


> [!NOTE]  
> If you want to pass or tune additional parameters, customise `./start_server.sh` before running `docker build ...`
