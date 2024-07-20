ARG CUDA_IMAGE="12.5.1-devel-ubuntu22.04"
FROM nvidia/cuda:${CUDA_IMAGE}

# We need to set the host to 0.0.0.0 to allow outside access
ENV HOST 0.0.0.0

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y git build-essential \
    python3 \
    python3-pip \
    gcc \
    wget \
    ocl-icd-opencl-dev \
    opencl-headers clinfo \
    libclblast-dev \
    libopenblas-dev \
    && mkdir -p /etc/OpenCL/vendors && echo "libnvidia-opencl.so.1" > /etc/OpenCL/vendors/nvidia.icd \ 
    && apt-get clean 

COPY . .

# setting build related env vars
ENV CUDA_DOCKER_ARCH=all
# Orig - ENV LLAMA_CUBLAS=1
ENV LLAMA_CUDA=1

# Install depencencies
RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install --upgrade pip pytest cmake scikit-build setuptools fastapi uvicorn sse-starlette pydantic-settings starlette-context

# Install llama-cpp-python (build with cuda)
# Note, some builds do not have a linux whl file.  Goto https://github.com/abetlen/llama-cpp-python/releases
#       Find the latest release that has a linux whl file (see Assets for the release)
#       Then defeine that build in the following line
#       If the latest build does not include a linux whl file, AND an appropriate build is not specified, then the build will fail.
#       ***** Make sure to specify the x.x.x-cu12X release for the Cuda supported whl file.  Use copy the link to the desired whl file and use below.

# From a base example:
# pip install --no-cache-dir llama-cpp-python==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu123

RUN CMAKE_ARGS="-DGGML_CUDA=on" pip install llama-cpp-python==0.2.82 \
        --extra-index-url https://github.com/abetlen/llama-cpp-python/releases/download/v0.2.82-cu124/llama_cpp_python-0.2.82-cp312-cp312-linux_x86_64.whl \
        --verbose;

# Clean up apt cache
RUN rm -rf /var/lib/apt/lists/*


# Old
# RUN CMAKE_ARGS="-DLLAMA_CUBLAS=on" pip install llama-cpp-python

# --------------------------------------------------------
# -- Updating Server Settings (API Key, SSL Key and Cert, etc.)
# --------------------------------------------------------
# If additional settings are desire, then copy the settings.py file to the directory with the Dockerfile
#   update the settings.py with the Server Settings listed below, and copy into 
#   /usr/local/lib/python3.10/dist-packages/llama_cpp/server/ directory in the container.

# COPY settings.py /usr/local/lib/python3.10/dist-packages/llama_cpp/server/

# Server settings used to configure the FastAPI and Uvicorn server:
# - host: str = Field(default="localhost", description="Listen address")  -- May be set with Environment variables
# - port: int = Field(default=8000, description="Listen port")            -- May be set with Environment variables
# - ssl_keyfile: SSL key file for HTTPS                                   -- set in settings.py
# - ssl_certfile: SSL certificate file for HTTPS                          -- set in settings.py
# - api_key: API key for authentication. If set all requests need to be authenticated.   -- set in settings.py
# - interrupt_requests: Whether to interrupt requests when a new request is received.    -- set in settings.py
# - disable_ping_events: Disable EventSource pings (may be needed for some clients).     -- set in settings.py
# - root_path: The root path for the server. Useful when running behind a reverse proxy. -- set in settings.py


# Set environment variable for the host
#ENV HOST=0.0.0.0
#ENV PORT=8000

# Expose a port for the server
#EXPOSE 8000

# Run the server start script
# Run the server start script
#CMD ["/bin/sh", "/app/run.sh"]

# Default command
CMD python3 -m llama_cpp.server

