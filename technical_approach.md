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


## Embedding Model


## Vector Database

- ChromaDB
- 

## LLM Model


## User Interface






Public LLMs





















## The private LLM structure

Let’s start with a zoomed-out view of the components you need to create a local language model that can interact with your documents. In a previous article, I did a deep dive into [customizing ChatGPT](https://bdtechtalks.com/2023/05/01/customize-chatgpt-llm-embeddings/) with your own data and documents. Your local LLM will have a similar structure, but everything will be stored and run on your own computer:



3\. **Vector database**: A vector database is designed to store and retrieve embeddings. It can store the content of your documents in a format that can be easily compared to the user’s prompt. [Faiss](https://github.com/facebookresearch/faiss) is a library that you can use to add vector similarity comparisons on top of other data stores. But there are also a few open-source vector databases that you can install on your computer including [Qdrant](https://qdrant.tech/), Weaviate, and [Milvus](https://github.com/milvus-io/milvus).  

4\. **Knowledge documents**: A collection of documents that contain the knowledge your LLM will use to answer your questions. These documents depend on your application. For example, it can be a collection of PDF or text documents that contain your personal blog posts.

5\. **User interface**: The user interface layer will take user prompts and display the model’s output. This can be a simple command-line interface (CLI) or a more sophisticated web application such as [Streamlit](https://github.com/streamlit/streamlit). The user interface will send the user’s prompt to the application and return he model’s response to the user.

[![private GPT architecture](How%20to%20create%20a%20private%20ChatGPT%20that%20interacts%20with%20your%20local%20documents%20-%20TechTalks/private-LLM-architecture.jpg)](https://i0.wp.com/bdtechtalks.com/wp-content/uploads/2023/06/private-LLM-architecture.jpg?ssl=1)

private LLM architecture

## Private LLM workflow

Before you can use your local LLM, you must make a few preparations:

1\. Create a list of documents that you want to use as your knowledge base

2\. Break large documents into smaller chunks (around 500 words)

3\. Create an embedding for each document chunk

4\. Create a vector database that stores all the embeddings of the documents

If you add documents to your knowledge database in the future, you will have to update your vector database.

Now that our knowledge base and vector database are ready, we can review the workflow of the private LLM:

1\. The user enters a prompt in the user interface.

2\. The application uses the embedding model to create an embedding from the user’s prompt and send it to the vector database.

3\. The vector database returns a list of documents that are relevant to the prompt based on the similarity of their embeddings to the user’s prompt.

4\. The application creates a new prompt with the user’s initial prompt and the retrieved documents as context and sends it to the local LLM.

5\. The LLM produces the result along with citations from the context documents. The result is displayed in the user interface along with the sources.

[![private LLM ChatGPT workflow](How%20to%20create%20a%20private%20ChatGPT%20that%20interacts%20with%20your%20local%20documents%20-%20TechTalks/private-LLM-ChatGPT-workflow.jpg)](https://i0.wp.com/bdtechtalks.com/wp-content/uploads/2023/06/private-LLM-ChatGPT-workflow.jpg?ssl=1)

private LLM workflow

Open-source LLMs are much smaller than state-of-the-art models like ChatGPT and Bard and might not match them in every possible task. But [augmenting these language models](https://bdtechtalks.com/2023/04/03/augmented-language-models/) with your own documents makes them very powerful for tasks such as search and question-answering.

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

