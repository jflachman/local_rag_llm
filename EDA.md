### app.py

The main application script (`app.py`) is responsible for loading environment variables, processing PDF documents, and setting up the Streamlit application.

### 1. Loading Environment Variables

Environment variables are loaded using the `dotenv` library to securely manage sensitive information like the OpenAI API key.

### 2. Loading PDF Documents

PDF documents are loaded from the specified directory using `PyPDFDirectoryLoader`. This step ensures we can read the documents and convert them into a suitable format for processing.

### 3. Inspecting the Data

Upon loading, we inspect the contents of the documents to understand their structure and any associated metadata. This involves:
- Checking the number of documents.
- Viewing the first few documents to understand their content and structure.

![Files and Sentence count] https://github.com/jflachman/local_rag_llm/blob/main/docs/imgs/sentence_data.png
### 4. Basic Statistics

Calculate basic statistics about the text data, such as:
- Total number of documents.
- Average length of sentences within the documents.

### 5. Visualizing the Data

Visualize the distribution of document lengths or other relevant characteristics using plots or histograms.

![Sentence Data](/docs/imgs/sentence_data.png)

### 6. Text Preprocessing

The text content of the PDF documents is split into sentences using `nltk` sentence tokenizer. This step is crucial for processing long documents and making them manageable.

### 7. Analyzing the Sentences

Analyze the sentences to understand their distribution, length, and content. This helps in identifying any issues with the splitting logic and ensures the sentences are of appropriate size for embedding.

### 8. Saving to ChromaDB

The sentences are saved to ChromaDB, which uses OpenAI embeddings for efficient retrieval. This step involves clearing any existing data and persisting the new sentences.

### 9. Querying the Data

We query the stored data using a Retrieval-Augmented Generation (RAG) approach. This involves searching for relevant context in the sentences and generating a response based on the query.

### 10. Displaying Results in Streamlit

The generated response is displayed in the Streamlit application, providing an interactive interface for querying and viewing results.

## Conclusion

This document outlines the Exploratory Data Analysis (EDA) process for PDF document processing using Langchain and ChromaDB. By following these steps, the application effectively handles document processing, text splitting into sentences, embedding, storage, and querying. This thorough analysis ensures the data is appropriately processed and ready for further use in the application.