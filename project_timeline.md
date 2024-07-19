# Project Timeline

## Week 1: July 22 - July 28

**Goal**: Basic data ingestion and Docker setup.

- **July 22-23**:
  - **Task**: Prepare sample documents for ingestion.
  - **Details**: Collect or create a small set of sample documents to be used for ingestion.
  - **Deliverables**: Sample documents placed in `SOURCE_DOCUMENTS`.

- **July 24-25**:
  - **Task**: Implement and test the data ingestion script.
  - **Details**: Run the ingestion script to ensure documents are correctly ingested into the vector database.
  - **Deliverables**: Successfully ingested documents and verified database content.

- **July 26-28**:
  - **Task**: Add Docker support and create a Dockerfile.
  - **Details**: Write a Dockerfile and build the Docker image. Ensure the application runs correctly within the Docker container.
  - **Deliverables**: Dockerfile and working Docker image.

## Week 2: July 29 - August 1

**Goal**: Integrate and fine-tune the RAG model components and embedding model, develop a basic user interface using Streamlit, finalize LLM integration, and prepare for the final demonstration.

- **July 29-30**:
  - **Task**: Integrate the retriever and generator components.
  - **Details**: Ensure the RAG architecture components are correctly integrated and can retrieve and generate responses based on the ingested documents.
  - **Deliverables**: Working model integration.

- **July 31**:
  - **Task**: Chunk the text and integrate the embedding model.
  - **Details**: Implement text chunking to handle large documents. Choose an appropriate embedding model (e.g., FastEmbedEmbeddings, Hugging Face transformers) and integrate it for document vectorization.
  - **Deliverables**: Chunked texts, embedded documents, and a functional retrieval system.

- **July 31 - August 1**:
  - **Task**: Develop a basic UI using Streamlit.
  - **Details**: Create a simple web interface to upload documents, query the model, and display results.
  - **Deliverables**: Functional UI for interacting with the model.

- **August 1**:
  - **Task**: Finalize LLM integration and test the end-to-end system.
  - **Details**: Ensure the LLM responds accurately to queries using the embedded documents. Perform fine-tuning if necessary.
  - **Deliverables**: Fully integrated and functional RAG system.

- **August 1**:
  - **Task**: Final testing and validation.
  - **Details**: Run comprehensive tests to ensure the system works as expected. Validate responses with sample queries.
  - **Deliverables**: Final, tested project ready for demonstration.