## Table of Contents

 - [README](README.md)
 - [Project Proposal](project_proposal.md)
 - [Technical Approach](technical_approach.md)
 - [Application Packages](docs/application_packages.md) Used in this project
   - [Knowledge Documents](docs/knowledge_documents.md)
   - [User Interface](docs/user_interface.md)
   - [LLMs](docs/LLMs.md)
   - [Embeddings](docs/embedding.md)
   - [Vector Database](docs/vectorDB.md)


# Applications and Packages for Knowledge Based LLM

The application packages used in this project are described here.  More information on the details and options for the application components can be found in the following documents.


## Langchain or Llamaindex

- [Langchain](https://www.langchain.com/)
  - [Documentation](https://python.langchain.com/v0.2/docs/introduction/)
  - [Templates](https://templates.langchain.com/)
  - [Integrations](https://python.langchain.com/v0.2/docs/integrations/platforms/)


## Llamaindex

- [LlamaIndex](https://www.llamaindex.ai/open-source)
  - [Getting Started](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)


## Embedding Model

Embeddings encode complex, high-dimensional data into lower dimensional numeric space.  Using embeddings, prompts and response context can be matched by finding the closest embedded content in the embedding space.

The embedding model selected for this project is: **TBD**

This embedding model was selected for ......

## Vector Database

A Vector Database is designed to store and retrieve embeddings.  The vector database makes it possible to query with the embedded user prompt and return the documents that most closely match the embedding.

See VectorDB integrations in Langchain and Llamaindex

The vector database used in this project is: **TBD**
- ChromaDB??

This vector database was selected for ......


## LLM Model




## User Interface

**Note:**  This may come with Llamaindex.


## References:

- medium
  - [(Python) Streamlit + Local LLM](https://medium.com/@stefnestor/python-streamlit-local-llm-2aaa75961d03)
  - [Guide to Setting up Your Local LLM](https://medium.com/@marketing_novita.ai/guide-to-setting-up-your-local-llm-cc45b78413e0)
  - [Build RAG Application Using a LLM Running on Local Computer with GPT4All and Langchain](https://medium.com/rahasak/build-rag-application-using-a-llm-running-on-local-computer-with-gpt4all-and-langchain-13b4b8851db8)
  - [Using Retrieval Augmented Generation (RAG) to Enhance Local Large Language Models](https://medium.com/@uppadhyayraj/using-retrieval-augmented-generation-rag-to-enhance-local-large-language-models-e81b156f1457)
  - [Build RAG Application Using a LLM Running on Local Computer with Ollama Llama2 and LlamaIndex](https://medium.com/rahasak/build-rag-application-using-a-llm-running-on-local-computer-with-ollama-and-llamaindex-97703153db20)
  - [Use LlamaIndex and a Local LLM to Summarize YouTube Videos](https://medium.com/@bSharpML/use-llamaindex-and-a-local-llm-to-summarize-youtube-videos-29817440e671)
  - [Local RAG From Scratch](https://towardsdatascience.com/local-rag-from-scratch-3afc6d3dea08)

- Miscellaneous Articles
  - [How to create a private ChatGPT that interacts with your local documents](https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/)
  - [Run LLMs Locally: 7 Simple Methods](https://www.datacamp.com/tutorial/run-llms-locally-tutorial)
  - [Mastering RAG: How to Select an Embedding Model](https://www.rungalileo.io/blog/mastering-rag-how-to-select-an-embedding-model)
  - [Build an LLM RAG Chatbot With LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/)
  - [Fully local retrieval-augmented generation, step by step](https://www.infoworld.com/article/3715181/fully-local-retrieval-augmented-generation-step-by-step.html)
  - [ NLP | LLM | LangChain RAG | QA Data |](https://www.kaggle.com/code/yannicksteph/nlp-llm-langchain-rag-qa-data)
  - [Local LLM RAG Tutorial: Building a Retrieval Augmented Generation System with Llama 3 and LlamaIndex](https://anakin.ai/blog/local-rag-llm-tutorial/)
  - [A beginner's guide to building a Retrieval Augmented Generation (RAG) application from scratch](https://learnbybuilding.ai/tutorials/rag-from-scratch)

- Langchain
  - [Langchain - Build a Local RAG Application](https://python.langchain.com/v0.2/docs/tutorials/local_rag/)
  - [Run LLMs locally](https://python.langchain.com/v0.1/docs/guides/development/local_llms/)
  - [Build a Retrieval Augmented Generation (RAG) App](https://python.langchain.com/v0.2/docs/tutorials/rag/)
  - [Rag from Scratch](https://github.com/langchain-ai/rag-from-scratch)

- Llama-Index
  - [Using LLMs](https://docs.llamaindex.ai/en/stable/understanding/using_llms/using_llms/)
  - [LlamaIndex Private Setup](https://colab.research.google.com/drive/16QMQePkONNlDpgiltOi7oRQgmB8dU5fl?usp=sharing)
  - [Retrieval Augmented Generation (RAG) with Llama Index and Open-Source Models](https://christophergs.com/blog/ai-engineering-retrieval-augmented-generation-rag-llama-index)
  - [Using LlamaIndex and llamafile to build a local, private research assistant](https://www.llamaindex.ai/blog/using-llamaindex-and-llamafile-to-build-a-local-private-research-assistant)

- Github
  - [Langchain RAG tutorial](https://github.com/pixegami/langchain-rag-tutorial)
    - [Python RAG Tutorial with local LLM](https://www.youtube.com/watch?v=2TJxpyO3ei4) - Video
  - [Self RAG using local LLMs](https://langchain-ai.github.io/langgraph/tutorials/rag/langgraph_self_rag_local/)
  - **[Local LLM and RAG](https://github.com/amscotti/local-LLM-with-RAG)**
  - [Local RAG Llama Index](https://github.com/Otman404/local-rag-llamaindex)
  - Krish Naik
    - [Youtube channel](https://www.youtube.com/@krishnaik06/playlists) - Video
    - [Langchain examples](https://github.com/krishnaik06/Updated-Langchain/blob/main/README.md)
    - [More Langchain examples](https://github.com/krishnaik06/Complete-Langchain-Tutorials)
    - [LlamaIndex examples](https://github.com/krishnaik06/Llamindex-Projects)

- The Future with AI Agents and LLM OS
  - [AI LLM application pyramid](https://www.youtube.com/watch?v=F5nlMBVZxb4)
  - [AI Agents Tutorials](https://www.youtube.com/playlist?list=PLpdmBGJ6ELUJ9pOJt8gGPCqVw7wp2pFpM)

----
----
----
----
----
