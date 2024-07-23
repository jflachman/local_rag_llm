# Open-WebUI with Ollama

## References: 

 - https://docs.openwebui.com/getting-started/
 - https://docs.openwebui.com/tutorial/rag/#:~:text=Retrieval%20Augmented%20Generation%20(RAG)%20is,incorporating%20context%20from%20diverse%20sources.
 - 



docker run -d -p 3000:8080 --gpus=all -v C:/ML/DU/local_rag_llm/ollama:/root/.ollama -v C:/ML/DU/local_rag_llm/open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:ollama
