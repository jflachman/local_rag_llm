# How to use Dockerized Anything LLM

- https://docs.useanything.com/
- https://github.com/Mintplex-Labs/anything-llm/blob/master/README.md
- https://github.com/Mintplex-Labs/anything-llm/blob/master/docker/HOW_TO_USE_DOCKER.md


Run this in powershell terminal

    $env:STORAGE_LOCATION="$HOME\Documents\anythingllm"; `
    If(!(Test-Path $env:STORAGE_LOCATION)) {New-Item $env:STORAGE_LOCATION -ItemType Directory}; `
    If(!(Test-Path "$env:STORAGE_LOCATION\.env")) {New-Item "$env:STORAGE_LOCATION\.env" -ItemType File}; `
    docker run -d -p 3001:3001 `
    --cap-add SYS_ADMIN `
    -v "$env:STORAGE_LOCATION`:/app/server/storage" `
    -v "$env:STORAGE_LOCATION\.env:/app/server/.env" `
    -e STORAGE_DIR="/app/server/storage" `
    mintplexlabs/anythingllm;


