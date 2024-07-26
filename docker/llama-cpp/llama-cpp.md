## Llama-cpp-python TOC
1. [Overview](README.md)
2. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
3. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)
4. [Run the docker image (CUDA or CPU version)](startup-llama-cpp-docker.md)
5. **[Using Llama-cpp server](llama-cpp.md)**
6. [Server Configuration](server_config.md) using a `server.conf` file

---------
---------

# Using Llama-cpp-server

## Access the server

Once your server is running (given you are using port `8100`), you may access it here:  http://localhost:8100/docs

## Using the server from your code










## References

- https://python.langchain.com/v0.2/docs/integrations/llms/llamacpp/
- https://platform.openai.com/docs/api-reference/introduction
- https://llama-cpp-python.readthedocs.io/en/latest/
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)
- https://github.com/abetlen/llama-cpp-python
- https://github.com/ggerganov/llama.cpp/blob/master/examples/server/README.md
- 
### Typical Model Sizes

| Model |  Quantized size |
|------:|----------------:|
|    3B |            3 GB |
|    7B |            5 GB |
|   13B |           10 GB |
|   33B |           25 GB |
|   65B |           50 GB |
