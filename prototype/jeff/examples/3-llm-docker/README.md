# LLM Everywhere: Docker for Local and Hugging Face Hosting

- https://www.docker.com/blog/llm-docker-for-local-and-hugging-face-hosting/
- https://www.docker.com/blog/build-machine-learning-apps-with-hugging-faces-docker-spaces)


Read Token
` docker run -it -p 7860:7860 -e HUGGING_FACE_HUB_TOKEN="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" registry.hf.space/harsh-manvar-llama-2-7b-chat-test:latest python app.py`

Write Token
- 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

` docker run -it -p 7860:7860 -e HUGGING_FACE_HUB_TOKEN="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" registry.hf.space/harsh-manvar-llama-2-7b-chat-test:latest python app.py`

http://localhost:7860


`docker buildx  build -t local-llm:v1 .`

	
`docker run -it -p 7860:7860 -e HUGGING_FACE_HUB_TOKEN="YOUR_VALUE_HERE" local-llm:v1 python app.py`
