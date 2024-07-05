## Table of Contents

 - [README](README.md)
 - [Project Proposal](project_proposal.md)
 - [Technical Approach](technical_approach.md)
 - [Application Packages](docs/application_packages.md) Usedin this project
   - [Knowledge Documents](docs/knowledge_documents.md)
   - [User Interface](docs/user_interface.md)
   - [LLMs](docs/LLMs.md)
   - [Embeddings](docs/embedding.md)
   - [Vector Database](docs/vectorDB.md)


# LLM/RAG approach for Private Document Store

DU AI ML bootcamp final group project


## Executive Summary

The goal of this project is to implement a Local Language Model (LLM) capable of reviewing, summarizing, and leveraging proprietary documents to facilitate document management tasks. The LLM will run on a laptop equipped with a 6GB RTX 3060 GPU and 32GB RAM. The system will take a list of files as input, provide answers to questions about these files, summarize the content, and assist in writing new documents based on the provided information.

This project will be reused after the class for developing documentation from existing proprietary documents at students current employer.

## Project Description

This project aims to enhance document management by leveraging an LLM to process and understand proprietary documents. The LLM will be integrated into a local system that will ensure data security and compliance with privacy regulations. The key functionalities of the LLM will include document review, question answering, summarization, and document creation assistance.

## Project Proposal

The [Project Proposal](project_proposal.md) provides more details about the initial project concept and premiliminary approach.

## Project Approach

### Workflow

1. User enters a prompt
2. The application uses an embedding model to embed the prompt 
3. The prompt embedding is sent to the vector database
4. The vector database returns a list of documents that most closely match the prompt embedding.  This is the context provided to the LLM.
5. The application creates a new prompt using:
   1. The users original prompt
   2. A system prompt that provides a "persona" to use for the response
   3. The ***context*** - document text
6. This new prompt is sent to the Local LLM or alternatively a cloud based LLM API
7. The LLM produces a result based on the extended prompt using the best associated information in the Knowledge Base.

### Creating the knowledge base

1. Provide a list of Documents and Sources to use for the knowledge base.
2. Break the documents into smaller chunks
3. Create an embedding for each document chunk
4. Implement a vector database that stores the document embeddings


## Technical Approach

The description of the applications, packages and approach used for the project are described in the [Technical Approach](technical_approach.md).  There are tools that make developing a local LLM based solution simple to implement.  However, this project will implement each component to build the overall solution.

A summary of general considerations provided below.

1. **Knowledge Documents:** Options:
   1. Local Documents (pdf, html, text, etc)
   2. Internet Search Results
2. **Embedding Model:**
   1. The same ebedding model must be used to create the knowledge base and embed the users prompt.
3. **Vector DB:**
   1. Select a lightweight, easy to implement DB
4. **Large Language Model (LLM):** There are two approaches for an LLM. Both approaches work similarly.  The difference is the Robustness of the LLM model, the resources required and potential licensing requirements and costs.  Pros and cons of Public vs Private/Local LLMs are listed below
   1. Public LLM API:  
   2. Local Private LLM:
5. **User Interface:** There are two options for a user interface
   1. Use a simple terminal command line interface for the prompt and response
   2. Use a web based interface.  There are several approaches that may provide a relatively simple implementation.