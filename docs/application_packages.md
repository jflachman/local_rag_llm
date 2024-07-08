## Table of Contents

 - [README](../README.md)
 - [Project Proposal](project_proposal.md)
 - [Technical Approach](technical_approach.md)
 - [Application Packages](application_packages.md) Used in this project
   - [Knowledge Documents](knowledge_documents.md)
   - [User Interface](user_interface.md)
   - [LLMs](LLMs.md)
   - [Embeddings](embedding.md)
   - [Vector Database](vectorDB.md)
   - [Other Notes](misc_notes.md)
 - [References](references.md)


# Application Packages

The application packages used in this project are described here.  More information on the details and options for the application components can be found in the following documents.


## Langchain or Llamaindex

- [Let’s talk about LlamaIndex and LangChain](https://superwise.ai/blog/lets-talk-about-llamaindex-and-langchain/)
- [Langchain](https://www.langchain.com/)
  - [Documentation](https://python.langchain.com/v0.2/docs/introduction/)
  - [Templates](https://templates.langchain.com/)
  - [Integrations](https://python.langchain.com/v0.2/docs/integrations/platforms/)


## Llamaindex

- [LlamaIndex](https://www.llamaindex.ai/open-source)
  - [Getting Started](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)
  - [A new document summary index for LLM powered QA systems](https://www.llamaindex.ai/blog/a-new-document-summary-index-for-llm-powered-qa-systems-9a32ece2f9ec)

Libraries:
-  SimpleDirectoryReader
-  LLMPredictor
-  ServiceContext
-  ResponseSynthesizer
-  GPTDocumentSummaryIndex
- from llama_index.indices.document_summary import DocumentSummaryIndexRetriever
- from llama_index.indices.document_summary import GPTDocumentSummaryIndex
- from langchain.chat_models import ChatOpenAI

## Langchain

Libraries:
- chat_models -> OpenAI

## Embedding Model


## Vector Database

See VectorDB integrations in Langchain and Llamaindex


- ChromaDB will be used for this solution
- 

## Local LLM server

Ollama
- [Ollama GPU support](https://github.com/ollama/ollama/blob/main/docs/gpu.md)
  

## LLM Model

- [llama3]

## User Interface



