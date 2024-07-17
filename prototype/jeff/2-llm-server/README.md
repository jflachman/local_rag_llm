**Prototypes Table of Contents**

0. [Prototypes Overview](../README.md)
1. [Build AIML python environment](../1-build-env/README.md)
2. [LLM Server](../2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
3. [Vector Database](../3-vectorDB/README.md)
4. [User Interface](../4-user-interface/README.md)
5. TBD - [RAG Workflow](../5-rag-workflow/README.md)
6. TBD - [RAG & UI integration](../6-rag-ui-integration/README.md)

---------
---------

# LLM Server Investigation - llama-cpp-python

## Overview  

**Objective:** host an OpenAI compliant server in docker running a local LLM model from Huggingface.

Steps:
1. Run llama-cpp-python examples in Jupyter
2. Run a stock docker container
    - Determine if this container satisfies step 3.
3. Build a docker container with:
    - CUDA GPU support
    - OpenAI compliant API

**Step 3 is TBD**

Note:  Local path to models for docker on WSL is:  `C:/ML/DU/local_rag_llm/models`.  Also, `/home/user/rag_llm` is a softlink to `/mnt/c/ML/CU/local_rag_llm`

## 1. llama-cpp-python example:

Ran example from sunny2309: [Llama CPP Turorial](llama-cpp-tutorial.ipynb)

- Ran perfectly with modifications for local llm `/home/user/rag_llm/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf`.  made this a variable llm_model.

## 2. Stock Docker Container

Tried out available docker image:

**generic**

`docker run --rm -it -p 8000:8000 -v /path/to/models:/models -e MODEL=/models/llama-model.gguf ghcr.io/abetlen/llama-cpp-python:latest`

**My parameters**

    `docker run -it -p 8100:8000 -v C:/ML/DU/local_rag_llm/models:/models -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf  ghcr.io/abetlen/llama-cpp-python:latest`

**Your parameters:**

- Try the my parameters version above, but modify `C:/ML/DU/local_rag_llm/db` to the location of the database on you local directory.

## 3. Create a custom container



### 3a. Build Dockerfile and Container

**TBD**


### 3b. Test


**TBD**
