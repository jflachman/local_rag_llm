## Llama-cpp-python TOC
1. [Overview](README.md)
2. [Create a custom Docker image with CUDA support and server.config](docker-build-llama-cpp-GPU.md)
3. [Create a custom Docker image with server.config](docker-build-llama-cpp-CPU.md)
4. [Run the docker image (CUDA or CPU version)](startup-llama-cpp-docker.md)
5. **[Using Llama-cpp server](llama-cpp.md)**
6. [Server Configuration](server_config.md) using a `server.conf` file

---------
---------

# Server Configuration

## 1. Server Configuration using a `server.config` file

The [CUDA enabled docker container](docker-build-llama-cpp-GPU.md) is built to allow an server.conf file to be passed when starting up the container.  A [CPU only image](docker-build-llama-cpp-cpu.md) is also available.  A good place to put this file is in the `/var/models` directory.  See the default [server.config](server.config) file there.  The file name is arbitrary.  So you could use `best_models.conf` for example.

    docker run -it -d -p 8000:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v C:/ML/DU/local_rag_llm/models:/var/model  jflachman/llama-cpp-python:v0.2.77-cuda /var/model/server.config

For more information on parameters for configuring the server see:

- [Server Options Reference](https://llama-cpp-python.readthedocs.io/en/latest/server/#server-options-reference)
- [Configuration and Multi-Model Support](https://llama-cpp-python.readthedocs.io/en/latest/server/#configuration-and-multi-model-support) - has a sample `server.config` and show how to configure/load multiple models.
- https://llama-cpp-python.readthedocs.io/en/latest/server/



## 2. Encryption & Authentication

**Encryption** is accomplished by setting the `ssl_keyfile` and the `ssl_certificate`.  There are many ways to generate these.  A google search should provide some.

Example: [How to generate a self-signed SSL certificate using OpenSSL](https://stackoverflow.com/questions/10175812/how-to-generate-a-self-signed-ssl-certificate-using-openssl)

This code will create `cert.pem` and `key.pem` files in the current directory.

        # interactive
        openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 365

        # non-interactive and 10 years expiration
        openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -sha256 -days 3650 -nodes -subj "/C=XX/ST=StateName/L=CityName/O=CompanyName/OU=CompanySectionName/CN=CommonNameOrHostname"


## 3. Authentication

**Authentication** can be accomplished with an `API_KEY`.  All authentication requests use this key.  This is typically a secret shared between the UI application and the LLM server.


## 4. References

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


