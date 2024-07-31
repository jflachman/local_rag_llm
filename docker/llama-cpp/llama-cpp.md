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

**NOTE:** in the following examples `Qwen2-0.5b-instruct` is the `model_alias` defined in the `server.config` file when you started the `llama-cpp-python` docker container.


- Startup an OpenAI client using the local server

      from openai import OpenAI
      client = OpenAI(
          api_key     ="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # can be anything
          base_url    ="http://localhost:8100/v1",  # NOTE: Replace with IP address and port of your llama-cpp-python server
      )

      model = "Qwen2-0.5b-instruct"


- **Alternate:** Start up a chat client using the local server

      from langchain_openai import ChatOpenAI
      model = ChatOpenAI(
          api_key     ="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  # can be anything
          base_url    ="http://localhost:8100/v1",  # NOTE: Replace with IP address and port of your llama-cpp-python server
          model="Qwen2-0.5b-instruct", )


- **Alternate:** Set OpenAI environment variables, then start-up OpenAI without api-key and base-url parameters.

      import os
      from openai import OpenAI
      from langchain_openai import ChatOpenAI
      
      os.environ["OPENAI_API_KEY"] = ( "sk-xxxxxxxxxx" ) # can be anything
      os.environ["OPENAI_API_BASE"] = "http://localhost:8100/v1"

  - Then startup Chatclient or Open regular client

        model = ChatOpenAI(model="Qwen2-0.5b-instruct" )

  - or

        client = OpenAI()
        model = "Qwen2-0.5b-instruct"





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
