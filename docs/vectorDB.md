## Table of Contents

 - [README](../README.md)
 - [Project Proposal](project_proposal.md)
 - [Technical Approach](technical_approach.md)
 - [Technical Implementation](../technical_implementation.md)
 - [Prototypes](../Prototypes/README.md) developed in support of the Technical Approach & Implementation
 - Research, Trades and References
   - [Knowledge Documents](knowledge_documents.md)
   - [User Interface](user_interface.md)
   - [LLMs](LLMs.md)
   - [Embeddings](embedding.md)
   - [Vector Database](vectorDB.md)
   - [Other Notes](misc_notes.md)
   - [References](references.md)

# Vector DB

3\. **Vector database**: A vector database is designed to store and retrieve embeddings. It can store the content of your documents in a format that can be easily compared to the user’s prompt. [Faiss](https://github.com/facebookresearch/faiss) is a library that you can use to add vector similarity comparisons on top of other data stores. But there are also a few open-source vector databases that you can install on your computer including [Qdrant](https://qdrant.tech/), Weaviate, and [Milvus](https://github.com/milvus-io/milvus).  