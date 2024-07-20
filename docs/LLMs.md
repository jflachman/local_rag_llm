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


# Large Language Models (LLMs)

1\. **Open-source LLM**: These are small [open-source alternatives to ChatGPT](https://bdtechtalks.com/2023/04/17/open-source-chatgpt-alternatives/) that can be run on your local machine. Some popular examples include Dolly, Vicuna, [GPT4All](https://gpt4all.io/index.html), and [llama.cpp](https://github.com/ggerganov/llama.cpp). These models are trained on large amounts of text and can generate high-quality responses to user prompts.



## 1. Trades:  Public vs Private LLMs (response from Co-pilot)

**Pros of Using LLMs in the Cloud:**
1. Scalability:
    - Cloud-based LLMs offer scalability by providing on-demand computing resources. Training and deploying LLMs often require high-end GPUs, which cloud services can readily provide1.
2. Cost Efficiency:
    - If you lack powerful hardware locally, using cloud services can be cost-effective. You pay only for the resources you use, and GPUs and CPUs are often available at affordable rates1.
3. Ease of Use:
    - Cloud platforms offer APIs, tools, and language frameworks that simplify building, training, and deploying machine learning models. Managed services handle infrastructure setup, maintenance, and security1.
4. Pre-Trained Models:
    - Cloud providers offer access to pre-trained LLMs that can be fine-tuned on custom datasets and deployed seamlessly1.

**Cons of Using LLMs in the Cloud:**
1. Resource Intensiveness:
    - Cloud-based LLMs can be resource-intensive during training and inference, leading to higher costs and potential bottlenecks1.
2. Privacy Concerns:
    - Storing data in the cloud may raise privacy and security issues, especially for sensitive information1.

**Pros of Using Local LLMs:**
1. Less Censorship:
    - Locally hosted LLMs allow more control over content and reduce dependency on external platforms.
2. Better Privacy:
    - Data remains within your local environment, enhancing privacy and reducing exposure to third parties.
3. Offline Access:
   - Local LLMs work even without an internet connection, ensuring uninterrupted usage.
4. Cost Savings:
    - Once set up, local LLMs avoid recurring cloud costs.
5. Customization:
   - Locally hosted models can be fine-tuned and customized to specific needs2.

**Challenges with LLMs:**
1. Bias Risk:
    - LLMs can inadvertently reproduce biases present in their training data, emphasizing the need for careful data curation and model monitoring3.


## 2. Local LLMs and LLM Servers

There are a number of open source LLM servers available.  Two popular servers are:

- [Ollama](https://ollama.com/)
- [Llamma-cpp-python]

Digging into some of the posts related to these two, trouble tickets and blog posts.  Comments indicate that Ollama is built ontop of llama-cpp.  

**Ollama**
- pros:
    - good documentation
    - easy to use
- cons:
    - Ollama seems to run 2x slower than llama-cpp.
    - Ollama has a limited number of models available

**Llama-cpp**
- pros
    - good documentation
    - easy to use
    - server access works the same as local server (one command and then the rest of the code works the same)
    - Can use any Huggingface model available in an accepted format
- cons
    - TBD

## 2.1 Llama-cpp-python server

See the [LLM-server](../prototype/jeff/2-llm-server/README.md) prototype for details:

**Resources:**

- https://llama-cpp-python.readthedocs.io/en/latest/
- https://github.com/abetlen/llama-cpp-python
- API: from local docker: http://localhost:8100/docs
- [API Reference](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)

**Startup:**

*Generic*

`docker run --rm -it -p 8000:8000 -v /path/to/models:/models -e MODEL=/models/llama-model.gguf ghcr.io/abetlen/llama-cpp-python:latest`

*My parameters*

    `docker run -it -p 8100:8000 -v C:/ML/DU/local_rag_llm/models:/models -e MODEL=/models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf  ghcr.io/abetlen/llama-cpp-python:latest`

**Check model:**

- http://localhost:8100/v1/models

**Access:**

- http://localhost:8100

** Models:**

See:  https://huggingface.co


## 2.2 Notes on Ollama Server running in a docker container

**Resources:**

- [Ollama is now available as an official Docker image](https://ollama.com/blog/ollama-is-now-available-as-an-official-docker-image)
- [GPU support in Docker Desktop](https://docs.docker.com/desktop/gpu/)

**Startup:**

`docker run -d --gpus=all -v C:/ML/DU/repos/projects/final/local_rag_llm:/root/.ollama -p 11434:11434 --name ollama ollama/ollama`

Now you can run a model like Llama 2 inside the container.  **Yes** Run the following command and it will load the model for use by the running container from the previous command.

`docker exec -it ollama ollama run llama3`

Check model:

`/show info`

**Access:**

- http://localhost:11434

** Models:**

More models can be found here:
- [Ollama library](https://ollama.com/library).
- [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file)
