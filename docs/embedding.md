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


# Embedding Models

**Executive Summary.**  

Embeddings encode complex, high-dimensional data into lower dimensional numeric space.  Using embeddings, prompts and response context can be matched by finding the closest embedded content in the embedding space.

Please see the references below for information on considerations for embedding.  Also see the referen

**Overview**
- **Embedding model options:** for the document and prompt embeddings in the RAG solution.
- **Embedding Research:** questions to Copilot with responses that help provide background and guidance on selecting embeddings.
- **References:** Useful Articles on embeddings

## Embedding model Options.

A discussion of the embedding model selected for the project is discussed in more detail in the [Application Packages](application_packages.md)

**Embedding Leader Board**
- Huggingface [Embedding Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

**OpenAI’s text-embedding-3-small:**

- This model is trained using **MRL (Multilingual Representations for Languages)** and delivers excellent performance even with small embedding dimensions (e.g., 256).
- It’s suitable for scenarios where you need compact embeddings without sacrificing retrieval quality1.

**Nomic’s Embed v1.5:**

- Nomic’s Embed is another powerful embedding model.
- It’s designed to encode text into dense vectors, capturing semantic information effectively.
- Consider using it for RAG tasks involving local knowledge documents.


## Embedding Research

### What is an Embedding Model? (Copilot)

An **embedding model** transforms complex, high-dimensional data (such as text, images, or sounds) into a simpler, lower-dimensional numeric space. This process involves encoding the data into **embeddings**, where each embedding is an array of numbers that collectively capture the key attributes of the original data1.

In essence, embeddings allow machine learning models to find similar objects. Unlike other ML techniques, embeddings are learned from data using various algorithms (such as neural networks) instead of explicitly requiring human expertise to define. They enable the model to learn complex patterns and relationships in the data, which would otherwise be impossible for humans to identify2. For example, OpenAI’s embedding implementation enables models like ChatGPT to understand relationships between different words and categories, resulting in more coherent and contextually relevant responses to user prompts and questions2.

In summary, embeddings serve as coordinates in a semantic space, making it easier for machine learning algorithms to process and find similarities among objects. They play a critical role in applications such as text and image search engines, recommendation systems, chatbots, and fraud detection2. 🌟

### What embedding models are best for a RAG solution of a local knowledge documents? (Copilot)

When selecting an embedding model for a **Retrieval-Augmented Generation (RAG)** solution that involves local knowledge documents, it’s essential to consider models that can efficiently capture semantic relationships and context. Here are some embedding models that work well for RAG with local knowledge documents:

**OpenAI’s text-embedding-3-small:**

- This model is trained using **MRL (Multilingual Representations for Languages)** and delivers excellent performance even with small embedding dimensions (e.g., 256).
- It’s suitable for scenarios where you need compact embeddings without sacrificing retrieval quality1.

**Nomic’s Embed v1.5:**

- Nomic’s Embed is another powerful embedding model.
- It’s designed to encode text into dense vectors, capturing semantic information effectively.
- Consider using it for RAG tasks involving local knowledge documents.

Remember that the choice of an embedding model significantly impacts the overall success of your RAG system. Evaluate the vector dimensions, average retrieval performance, and model size to make an informed decision


### Why do we use an embedding model in a RAG/LLM solution?** (Copilot)

In the context of **Retrieval-Augmented Generation (RAG) ** and ** Language Model (LLM)** solutions, embedding models play a crucial role. Let’s explore why we use them:

**Embeddings**: These are dense, continuous vectors that represent text in a high-dimensional space. Each word or token is mapped to an embedding vector, capturing semantic relationships and meanings. In RAG and LLMs, embeddings serve as coordinates in a semantic space, allowing efficient retrieval and context understanding.

**Applications of Embeddings:**
- **Question Answering (QA)**: Embeddings enhance QA systems within RAG applications. By encoding questions and potential answers into high-dimensional vectors, embeddings facilitate accurate matching between queries and context, leading to more precise and contextually relevant answers.
- **Conversational Search**: Conversations involve dynamic contexts. Embeddings represent nuances and relationships within dialogues, enabling RAG systems to retrieve relevant information and generate context-aware responses.
- **In-Context Learning (ICL)**: ICL benefits from dynamically retrieving demonstrations relevant to each input query. Embeddings help achieve this by encoding context-specific examples, enhancing learning efficiency and scalability.
- **Tool Fetching**: Embeddings improve tool recommendations by encoding both user requests and available tools, resulting in more accurate and user-friendly suggestions.

**Choosing the Right Embedding Model:**
- **Encoder Selection**: The choice of an embedding model significantly impacts RAG performance. High-quality embeddings lead to better retrieval results.
- **Criteria to Consider**:
  - **Vector Dimension**: Consider the dimensionality of the embedding vectors.
  - **Average Retrieval Performance**: Evaluate how well the embeddings perform in retrieval tasks.
  - **Model Size**: Consider the trade-off between model size and performance1.

In summary, embeddings are essential for precise and contextually relevant outputs in RAG and LLM applications. Choosing the right embedding model is critical for successful system performance. 🚀




## References

- [Mastering RAG: How to Select an Embedding Model](https://www.rungalileo.io/blog/mastering-rag-how-to-select-an-embedding-model)
- [Embeddings: What they are and why they matter](https://simonwillison.net/2023/Oct/23/embeddings/)