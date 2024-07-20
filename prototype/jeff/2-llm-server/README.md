**Prototypes Table of Contents**

0. [Prototypes Overview](../README.md)
1. [Build AIML python environment](../1-build-env/README.md)
2. [LLM Server](../2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
   1. [Llama-cpp-python](llama-cpp/README.md)
   2. [Ollama](ollama/README.md)
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
1. Run LLM server examples in Jupyter
2. Run a stock docker container
    - Determine if this container satisfies step 3.
3. Build a docker container with:
    - CUDA GPU support
    - OpenAI compliant API
4. Refine approach to using the selected LLM server


## Summary

Two technologies were examined:  llama-cpp-python and Ollama.

### [Llama-cpp-python](llama-cpp/README.md)

The goal was to deploy of CUDA version of Llama-cpp-python in Docker.  However, some issues that "appear" to be in my docker environment and nuances of llama-cpp-python prevented creating a cuda enabled docker container.  I am working in the llama-cpp-python discussion section on github to find a resolution.

Therefore, the rest of this discussion is halted mid-development until the CUDA docker solution is resolved.  Therefore the [llama-cpp-python investigation](llama-cpp/README.md) documentation may need refinement.


### [Ollama](ollama/README.md)

Originally llama-cpp-python was investigated because it provides easy integration with Huggingface and is reported to run faster than Ollama.  However docker build issues for CUDA became a blocker.

Ollama benefits and solutions:
- Ollama supports GPUs with their stock docker container.
- There is a method to use almost any huggingface model with Ollama.  It just requires a Modelfile that defines the Template for the selected model.

Ollama was chosen as the preferred server because it provides the best solution that fits within the short timeframe of this project.
