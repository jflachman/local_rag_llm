## Llama-cpp-python TOC
1. [Overview](README.md)
2. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
3. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)
4. [Run the docker image (CUDA or CPU version)](startup-llama-cpp-docker.md)
5. **[Using Llama-cpp server](llama-cpp.md)**
6. [Server Configuration](server_config.md) using a `server.conf` file

---------
---------

# Llama-cpp-python Server

## Executive Summary

Reference: CoPilot

`llama-cpp-python` is a Python package that provides bindings for the `llama.cpp` library, which implements Meta’s LLaMA (Large Language Model Meta AI) architecture in efficient C++. This integration allows developers to leverage the speed and efficiency of C++ within the flexible and widely-used Python environment

**Key Features** of llama-cpp-python
1. Low-Level Access: Provides low-level access to the C API via a ctypes interface.
2. **High-Level Python API:** Offers a high-level Python API for text completion, similar to OpenAI’s API.
3. **Compatibility:** Compatible with LangChain and LlamaIndex, making it easier to integrate into existing workflows.
4. **Web Server:** Includes an OpenAI-compatible web server, allowing it to serve as a local Copilot replacement.
5. **Multiple Models:** Supports multiple models, function calling, and vision API23.

**Benefits of Using** llama-cpp-python
1. **Efficiency:** By leveraging C++ for core computations, llama-cpp-python provides high performance and efficiency, which is crucial for handling large language models.
2. **Portability:** Designed to run on consumer-grade hardware, including personal computers and laptops, without requiring high-end GPUs or specialized hardware4.
3. **Flexibility:** Combines the computational efficiency of C++ with the ease of use of Python, making it suitable for a wide range of applications5.
4. **Universal Compatibility:** Its CPU-first design ensures less complexity and seamless integration into various programming environments1.
5. **Focused Optimization:** Optimized for the LLaMA models, enabling precise and effective improvements in performance1.


## Instructions

Steps to run and use Llama-cpp.server:

1. [Define your server configuration](server_config.md) (server.config)
2. [Startup the server in docker](startup-llama-cpp-docker.md)
3. [Access lama-cpp.server from your code](llama-cpp.md)

If you need to modify the docker container, then see:

1. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
2. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)


## [!NOTE] an alternate to llama-cpp-python is the base llama-cpp in docker

However, this is not covered in this project.

- https://github.com/ggerganov/llama.cpp/blob/master/docs/docker.md