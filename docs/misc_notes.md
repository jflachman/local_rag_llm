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

## RAG Prompting

Creating the Prompts for a Retrieval Augmented Generation (RAG) is complex.  There is a very good discussion here:

- https://community.openai.com/t/prompt-engineering-for-rag/621495/16
- https://www.promptingguide.ai/research/rag
- https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts
- https://platform.openai.com/docs/guides/chat-completions
- Great Example using our technologies: https://github.com/Quad-AI/LLM
- 

## PrivateGPT

By using a local language model and vector database, you can maintain control over your data and ensure privacy while still having access to powerful language processing capabilities. The process may require some technical expertise, but there are many resources available online to help you get started.

One solution is [PrivateGPT](https://github.com/imartinez/privateGPT), a project hosted on GitHub that brings together all the components mentioned above in an easy-to-install package. PrivateGPT includes a language model, an embedding model, a database for document embeddings, and a command-line interface. It supports several types of documents including plain text (.txt), comma-separated values (.csv), Word (.docx and .doc), PDF, Markdown (.md), HTML, Epub, and email files (.eml and .msg).

To use PrivateGPT, you’ll need Python installed on your computer. You can start by cloning the PrivateGPT repository on your computer and install the requirements:

```
git clone https://github.com/imartinez/privateGPT.git
cd privateGPT/
pip install -r requirements.txt
```

Next, you need to download a pre-trained language model on your computer. Create a “models” folder in the PrivateGPT directory and move the model file to this folder. PrivateGPT is configured by default to work with GPT4ALL-J (you can download it [here](https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin)) but it also supports llama.cpp. These are both open-source LLMs that have been trained for instruction-following (like ChatGPT). They have also been designed to run on computers with consumer-grade hardware. Llama.cpp works especially well on Mac computers with M1 processors.

Next, you have to create your knowledge base. PrivateGPT has a “source\_documents” folder where you must copy all your documents. After that, you must populate your vector database with the embedding values of your documents. Fortunately, the project has a script that performs the entire process of breaking documents into chunks, creating embeddings, and storing them in the vector database:

```
python ingest.py
```

Behind the scenes, PrivateGPT uses LangChain and SentenceTransformers to break the documents into 500-token chunks and generate embeddings. And it uses DuckDB to create the vector database. The result is stored in the project’s “db” folder. One thing to note is that LangChain needs to be connected to the internet to download the pre-trained embedding model. After that, all processing takes place on your own computer and you don’t need internet connectivity.

Depending on the number of documents that you have, creating the vector database might take several minutes. Once the preparation is finished, you can start the model with the following command:

```
python privateGPT.py
```

And then you can start talking to your local LLM with no strings attached. It will answer your questions and provide up to four sources from your knowledge base for each reply. PrivateGPT is an experimental project. It is not fast (it can take 20-30 seconds to respond) and is not optimized for every type of hardware. Its installation might also run into bugs based on your operating system and hardware. But it is surely a preview of one of the many directions the field is taking and the [powerful applications that open-source LLMs can unlock](https://bdtechtalks.com/2023/05/29/open-source-llms-cerebras-gpt/).
