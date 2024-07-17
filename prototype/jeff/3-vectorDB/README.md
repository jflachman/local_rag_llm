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

# Vector Database Investigations

## Overview

**Objective:** host a persistent vector database using ChromaDB running in docker with the persistent data store on my local hard drive.

1. Host chromaDB in docker
2. Determine how to host the database on the local drive
3. Initialize the DB for use in the RAG / LLM solution

## 1. Docker Execution

Started directly with a docker image.  Container ran perfectly.  However, need to determine how to initialize the DB.

**Generic:**

`docker run -d --rm --name chromadb -v ./chroma:/chroma/chroma -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE chromadb/chroma:latest`

**My Parameters:**

`docker run -d --name chromadb -v C:/ML/DU/local_rag_llm/db:/chroma/chroma -p 8200:8000 -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE chromadb/chroma:latest`

**Your parameters:**

- Try the my parameters version above, but modify `C:/ML/DU/local_rag_llm/db` to the location of the database on you local directory.

## 2. Persistence method

**TBD**


## 3. Database initialization

**TBD**

## 4. Test

**TBD**

## 5. Documentation:

- https://cookbook.chromadb.dev/running/running-chroma/#docker
- **API** http://localhost:8200/docs

