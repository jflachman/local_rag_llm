# LLama

[llama-cpp-python](https://github.com/abetlen/llama-cpp-python) container with cuda support

based on [3x3cut0r/llama-cpp-python](https://github.com/3x3cut0r/docker/blob/main/llama-cpp-python)

docker image: [afpro/cuda-llama-cpp-python](https://hub.docker.com/repository/docker/afpro/cuda-llama-cpp-python)

## requirement

* llama model at '/model.gguf'
* at least 20G VRAM and RAM

## api

`/v1` as openai protocol base url

`GET /health`  return `200`, needed by hugging face endpoint

### details

```text
Route(path='/openapi.json', name='openapi', methods=['GET', 'HEAD'])
Route(path='/docs', name='swagger_ui_html', methods=['GET', 'HEAD'])
Route(path='/docs/oauth2-redirect', name='swagger_ui_redirect', methods=['GET', 'HEAD'])
Route(path='/redoc', name='redoc_html', methods=['GET', 'HEAD'])
RouteErrorHandler(path='/v1/engines/copilot-codex/completions', name='create_completion', methods=['POST'])
RouteErrorHandler(path='/v1/completions', name='create_completion', methods=['POST'])
RouteErrorHandler(path='/v1/embeddings', name='create_embedding', methods=['POST'])
RouteErrorHandler(path='/v1/chat/completions', name='create_chat_completion', methods=['POST'])
RouteErrorHandler(path='/v1/models', name='get_models', methods=['GET'])
RouteErrorHandler(path='/extras/tokenize', name='tokenize', methods=['POST'])
RouteErrorHandler(path='/extras/tokenize/count', name='count_query_tokens', methods=['POST'])
RouteErrorHandler(path='/extras/detokenize', name='detokenize', methods=['POST'])
RouteErrorHandler(path='/health', name='heath_check', methods=['GET'])
```

