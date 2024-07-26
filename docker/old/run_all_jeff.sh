#!/bin/bash



# docker run -it -d -p 8100:8000 \
#     --name Llama-cpp \
#     -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf \
#     -v /ML/DU/local_rag_llm/models:/var/model \
#     ghcr.io/abetlen/llama-cpp-python:v0.2.77

# docker stop Llama-cpp
# docker rm Llama-cpp

docker run -it -d \
    --name Llama-cpp \
    -p 8100:8000 \
    -v //c/ML/DU/local_rag_llm/models:/var/model  \
    jflachman/llama-cpp-python:v0.2.77-cpu


docker run -it -d --name chromaDB -p 8200:8000 -e IS_PERSISTENT=TRUE -e ANONYMIZED_TELEMETRY=TRUE -v /ML/DU/local_rag_llm/db:/chroma/chroma chromadb/chroma:latest`

# --------------------------------------------------------
# Define Docker Commands
# --------------------------------------------------------
# chroma =    `docker run -it -d \
#             --name chromaDB \
#             -p 8200:8000 \
#             -e IS_PERSISTENT=TRUE \
#             -e ANONYMIZED_TELEMETRY=TRUE \
#             -v /ML/DU/local_rag_llm/db:/chroma/chroma \
#             chromadb/chroma:latest`

# run_llama_cpp_stock() {
#     docker run -it -d \
#     --name Llama-cpp \
#     -p 8100:8000 \
#     -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf \
#     -v /ML/DU/local_rag_llm/models:/var/model \
#     ghcr.io/abetlen/llama-cpp-python:v0.2.79
# }



# run_llama_cpp_cpu() {
#     docker run -it -d \
#         --name Llama-cpp \
#         -p 8100:8000 \
#         -v /ML/DU/local_rag_llm/models:/var/model  \
#         -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf \
#         jflachman/llama-cpp-python:v0.2.77-cpu

# #        -e SERVER="--config_file /var/model/server.config" \
#         #/var/model/server.sh
# #        //var/model/server.config
# #    docker run -it -d --name Llama-cpp -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v //ML/DU/local_rag_llm/models://var/model jflachman/llama-cpp-python:v0.2.77-cuda /var/model/server.config
#     # docker run -it -d -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v /ML/DU/local_rag_llm/models:/var/model  jflachman/llama-cpp-python:v0.2.77-cuda //var/model/server.config
# }

# run_llama_cpp_cuda() {
docker run -it -d --name Llama-cpp -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf -v /c/ML/DU/local_rag_llm/models:/var/model jflachman/llama-cpp-python:v0.2.77-cuda
# #        //var/model/server.config
# #    docker run -it -d --name Llama-cpp -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v //ML/DU/local_rag_llm/models://var/model jflachman/llama-cpp-python:v0.2.77-cuda /var/model/server.config
#     # docker run -it -d -p 8100:8000 --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 -v /ML/DU/local_rag_llm/models:/var/model  jflachman/llama-cpp-python:v0.2.77-cuda //var/model/server.config
# }

# run_llama_cpp_cuda_simple() {
#     docker run -it -d -p 8100:8000 \
#     --name Llama-cpp \
#     --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 \
#     -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf \
#     -v /ML/DU/local_rag_llm/models:/var/model \
#     jflachman/llama-cpp-python:v0.2.77-cuda-simple 
# #    ghcr.io/abetlen/llama-cpp-python:v0.2.79
# #    jflachman/llama-cpp-python:v0.2.83-cpu
# }

# run_llama_cpp_stock() {
#     docker run -it -d -p 8100:8000 \
#     --name Llama-cpp \
#     -e MODEL=/var/model/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf \
#     -v /ML/DU/local_rag_llm/models:/var/model \
#     ghcr.io/abetlen/llama-cpp-python:v0.2.77
# }

# docker rm Llama-cpp

# #run_llama_cpp_cpu
# #run_llama_cpp_cuda
# # run_llama_cpp_cuda_simple
# run_llama_cpp_stock


# # --------------------------------------------------------
# # Startup chromaDB
# # --------------------------------------------------------
# if [ "$(docker ps -a -q -f name=chromaDB)" ]; 
# then
#     if [ "$(docker ps -aq -f status=exited -f name=chromaDB)" ];
#     then
#         # Container Exists: Exited
#         echo "**ChromaDB container Exists: Exited - remove and restart container"
#         # cleanup
#         docker rm chromaDB
#         # Start ChromaDB
#         docker run -it -d \
#             --name chromaDB \
#             -p 8200:8000 \
#             -e IS_PERSISTENT=TRUE \
#             -e ANONYMIZED_TELEMETRY=TRUE \
#             -v /ML/DU/local_rag_llm/db:/chroma/chroma \
#             chromadb/chroma:latest
#     else  
#         # Container Exists: Running
#         echo "**ChromaDB container Exists - No change required"
#     fi
# else
#     # Container Does NOT Exist
#     echo "**ChromaDB container does NOT Exist - start container"
#     # Start ChromaDB
#     docker run -it -d \
#         --name chromaDB \
#         -p 8200:8000 \
#         -e IS_PERSISTENT=TRUE \
#         -e ANONYMIZED_TELEMETRY=TRUE \
#         -v /ML/DU/local_rag_llm/db:/chroma/chroma \
#         chromadb/chroma:latest
# fi


# # --------------------------------------------------------
# # Startup Llama-cpp Server
# # --------------------------------------------------------

# if [ "$(docker ps -a -q -f name=Llama-cpp)" ]; 
# then
#     if [ "$(docker ps -aq -f status=exited -f name=Llama-cpp)" ];
#     then  
#         # Container Exists: Exited
#         echo "**Llama-cpp container Exists: Exited - remove and restart container"
#         # cleanup
#         docker rm Llama-cpp
#         # Start Llama-cpp
#         docker run -it -d \
#             --name Llama-cpp \
#             -p 8100:8000 \
#             --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 \
#             -v /ML/DU/local_rag_llm/models:/var/model  \
#             jflachman/llama-cpp-python:v0.2.77-cuda \
#             /var/model/server.config
#     else  
#         # Container Exists: Running
#         echo "**Llama-cpp container Exists - No change required"
#     fi
# else
#     # Container Does NOT Exist
#     # Start Llama-cpp
#     echo "**Llama-cpp container does NOT Exist - start container"
#     docker run -it -d \
#         --name Llama-cpp \
#         -p 8100:8000 \
#         --gpus=all --cap-add SYS_RESOURCE -e USE_MLOCK=0 \
#         -v /ML/DU/local_rag_llm/models:/var/model  \
#         jflachman/llama-cpp-python:v0.2.77-cuda \
#         /var/model/server.config
# fi

# # --------------------------------------------------------
# # Startup Local_RAG Server
# # --------------------------------------------------------

# # if [ "$(docker ps -a -q -f name=Local_RAG)" ]; 
# # then
# #     if [ "$(docker ps -aq -f status=exited -f name=Local_RAG)" ];
# #     then  
# #         # Container Exists: Exited
# #         echo "**Local_RAG container Exists: Exited - remove and restart container"
# #         # cleanup
# #         docker rm Local_RAG
# #         # Start Local_RAG
# #         docker run -it -d \
# #             --name Local_RAG \
# #             -p 8100:8000 \
# #             jflachman/local_rag:v0.1
# # #    else  
# #         # Container Exists: Running
# #         echo "**Local_RAG container Exists - No change required"
# #     fi
# # else
# #     # Container Does NOT Exist
# #     echo "**Local_RAG container does NOT Exist - start container"
# #     # Start Local_RAG
docker run -it -d --name Local_RAG -p 8100:8000 jflachman/local_rag:v0.1
# # fi
