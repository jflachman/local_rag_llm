**Prototypes Table of Contents**

0. [Prototypes Overview](../../README.md)
1. [Build AIML python environment](../../1-build-env/README.md)
2. [LLM Server](../2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
   1. [Llama-cpp-python](../llama-cpp/README.md)
   2. [Ollama](../ollama/README.md)3. [Vector Database](../../3-vectorDB/README.md)
4. [User Interface](../../4-user-interface/README.md)
5. TBD - [RAG Workflow](../../5-rag-workflow/README.md)
6. TBD - [RAG & UI integration](../../6-rag-ui-integration/README.md)

---------
---------

# LLM Server Investigation - Ollama Server

## Overview  

**Objective:** host an OpenAI compliant server in docker running a local LLM model from Huggingface.

Steps:
1. Run ollama examples in Jupyter
2. Run a stock docker container
    - Determine if this container supports GPU.
3. Determine how to load models
4. Import Huggingface models
5. Work through some Ollama use cases
6. Stretch - Security: SSL, API-KEY

## 1. ollama example:

- Ran perfectly with modifications for local llm `/home/user/rag_llm/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf`.  made this a variable llm_model.

## 2. Stock Docker Container

Tried out available docker image:

- **generic**

      docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

- **My parameters**

      docker run -d --gpus=all -v C:/ML/DU/models:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

- **Your parameters:**

  - Try the my parameters version above, but modify `C:/ML/DU/local_rag_llm/db` to the location of the database on you local directory.


## 3. Load & Run Ollama model



## 3. Load & Run a Model


docker exec -it ollama ollama run llama3

## References

- https://github.com/ollama/ollama/blob/main/README.md#quickstart
- Docker: https://hub.docker.com/r/ollama/ollama
- Ollama Models: https://ollama.com/library
- Importing models: https://github.com/ollama/ollama/blob/main/docs/import.md
- Examples: https://github.com/ollama/ollama/tree/main/examples
- Ollama API: https://github.com/ollama/ollama/blob/main/docs/api.md
- 

### Huggingface Leaderboards

- All Leaderboards: https://huggingface.co/spaces?search=leaderboard
- Model Leaderboard:
  - https://huggingface.co/open-llm-leaderboard
  - https://huggingface.co/collections/open-llm-leaderboard/
  - llm-leaderboard-best-models-652d6c7965a4619fb5c27a03
  - https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard
- Ebedding Leaderboard
  - https://huggingface.co/spaces/mteb/leaderboard