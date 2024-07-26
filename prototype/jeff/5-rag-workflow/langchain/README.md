# Using Langchain for RAG Workflow

## References

- https://python.langchain.com/v0.2/docs/tutorials/
- [Conversational RAG](https://python.langchain.com/v0.2/docs/tutorials/qa_chat_history/)



## Technical Integration 

- Many solutions use `OpenAI` with something like the following:

        import getpass
        import os

        os.environ["OPENAI_API_KEY"] = getpass.getpass()

        from langchain_openai import ChatOpenAI

        llm = ChatOpenAI(model="gpt-4o-mini")

- This seems to create an LLM connection directly to OpenAI.  

**Question** How do we do something similar to our local LLM server using [llama-cpp-python](../../../../docker/llama-cpp/README.md)

See these sample Jupyter Notebooks from [Llama-cpp-python examples](https://github.com/abetlen/llama-cpp-python/tree/main/examples) for uses of the OpenAPI interface to web server.

- [gradio_chat](https://github.com/abetlen/llama-cpp-python/tree/main/examples/gradio_chat)
- [high_level_API](https://github.com/abetlen/llama-cpp-python/tree/main/examples/high_level_api)
- [notebooks](https://github.com/abetlen/llama-cpp-python/tree/main/examples/notebooks) See: - [multimodal.ipynb](https://github.com/abetlen/llama-cpp-python/tree/main/examples/notebooks/Multimodal.ipynb), [Clients.ipynb](https://github.com/abetlen/llama-cpp-python/tree/main/examples/notebooks/Clients.ipynb), [Guidance.ipynb](https://github.com/abetlen/llama-cpp-python/tree/main/examples/notebooks/Guidance.ipynb)
- [ray](https://github.com/abetlen/llama-cpp-python/tree/main/examples/ray) README for curl command.
- Debug with OpenAI API: https://github.com/openai/openai-python

**Solution**

- define the OPENAI Base and Host as your local [llama-cpp-python](../../../../docker/llama-cpp/README.md) server

        import os

        os.environ["OPENAI_API_KEY"] = (
            "sk-xxxxxxxxxxxxxxxxxxx"  # can be anything
        )
        os.environ["OPENAI_API_BASE"] = "http://localhost:8100/v1"
        os.environ["OPENAI_API_HOST"] = "http://localhost:8100"

- Option 2

        from openai import OpenAI

        client = OpenAI(base_url="http://localhost:8000/v1", api_key="llama.cpp")

        model = "gpt-3.5-turbo"



