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


# Large Language Models (LLMs)

1\. **Open-source LLM**: These are small [open-source alternatives to ChatGPT](https://bdtechtalks.com/2023/04/17/open-source-chatgpt-alternatives/) that can be run on your local machine. Some popular examples include Dolly, Vicuna, [GPT4All](https://gpt4all.io/index.html), and [llama.cpp](https://github.com/ggerganov/llama.cpp). These models are trained on large amounts of text and can generate high-quality responses to user prompts.



## Trades:  Public vs Private LLMs (response from Co-pilot)

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
