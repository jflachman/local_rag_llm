**Prototypes Table of Contents**

[Main Readme](../README.md)

1. [Build AIML python environment](1-build-env/README.md)
2. [LLM Server](2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
3. [Vector Database](3-vectorDB/README.md)
4. [User Interface](4-user-interface/README.md)
5. TBD - [RAG Workflow](5-rag-workflow/README.md)
6. TBD - [RAG & UI integration](6-rag-ui-integration/README.md)

---------
---------

# prototype work

The page documents the steps taking in the **investigation of technologies** and solutions for developing a RAG LLM solution.  It does not include all the research performed on RAG, LLM, alternative technologies, trade studies, etc.  That research is documented elsewhere.  Rather this documents steps in getting the chosen technologies up and running.

## Investigation Overview

**Objective:** Create a full persistent rag solution running in docker containers.

The investigation will look at the following:

1. Evaluate **Llama-cpp-python** to host an OpenAI compliant server in docker running a local LLM model from Huggingface
2. Evaluate 

## Prototypes

1. [Setup a WSL ubuntu AIML environment](1-build-env/README.md)
2. [llama-ccp-python](2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
3. [Vector Database](3-vectorDB/README.md) with local DB persistence *(deploy target: **docker**)*
4. [User Interface](4-user-interface/README.md) frameworks  *(deploy target: **docker**)*
5. TBD - [RAG Workflow](5-rag-workflow/README.md) Develop a rag workflow using 2 & 3.
6. TBD - [RAG & UI integration](6-rag-ui-integration/README.md) with updated Docker deployment.


## Examples to try: from multiple github & medium sources

### LLM Server Approach (examples)

1. Llama-ccp-python - [How to Run LLMs in a Docker Container](examples/1-llama-cpp/README.md) LLM Server
2. [Llama-cpp-python Docker CUDA](examples/2-llama-cpp-cuda/README.md) LLM Server
3. llm-docker - [LLM Everywhere: Docker for Local and Hugging Face Hosting](examples/3-llm-docker/README.md) LLM Server
4. anything-llm - [How to use Dockerized Anything LLM](examples/4-anything-llama/README.md) LLM Server
5. [download-llm](examples/5-download-llm/README.md) huggingface hub
6. [Retrieval Augmented Generation (RAG) with Llama Index and Open-Source Models](examples/6-rag-llm-opensourceLLMs/README.md)
7. [LlamaIndex-RAG-WSL-CUDA](examples/7-LlamaIndex-RAG-WSL-CUDA/README.md)
- [Models](models/README.md) LLM Server
  - Downloaded [models](../../models/README.md)

## References

### LLM Server approach
LLama-cpp-python

- https://llama-cpp-python.readthedocs.io/en/latest/
- https://github.com/abetlen/llama-cpp-python
- https://github.com/abetlen/llama-cpp-python/tree/main/docker

### RAG-LLM approaches

- youtube
    - https://www.youtube.com/watch?v=f-AXdiCyiT8
    - https://www.youtube.com/watch?v=hH4WkgILUD4
- github
    - https://github.com/krishnaik06/Llamindex-Projects/
    - https://github.com/marklysze/LlamaIndex-RAG-WSL-CUDA

- https://docs.unstructured.io/open-source/introduction/overview