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

# User Interface Investigation


## 1. Overview

**Objective:**  Select a UI framework and create a Dockerfile to host it in docker such that the RAG workflow in langchain may be added at a later time.

**Steps needed:**

1. Try different frameworks
2. Select a UI framework and run in a python file
3. Create a Docker container that runs the User interface.

There are many examples on github.com and medium.com.  [sunny2309](https://github.com/sunny2309) has simple examples.  I liked Sunny's examples because he had similar implementation with multiple UI frameworks including:

## 2. UI Evaluations and Opinions

### 2a. Chainlit



References:
- https://github.com/sunny2309/chainlit_chatbot
- https://github.com/Chainlit/chainlit
- https://docs.chainlit.io/get-started/overview


### 2b. Gradio

References:
- https://github.com/sunny2309/gradio_chatbot
- https://www.gradio.app/docs
- https://github.com/gradio-app/gradio


### 2c. Streamlit

References:
- https://github.com/sunny2309/streamlit_chatbot
- https://docs.streamlit.io/
- https://github.com/streamlit/streamlit


### 2d. Panel

References:
- https://github.com/sunny2309/panel_chatbot
- https://panel.holoviz.org/
- https://github.com/holoviz/panel


## UI Selection


## Dockerize UI


## Tests