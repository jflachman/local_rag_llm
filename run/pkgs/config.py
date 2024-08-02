# Fix this line to your repo
project_path    = "/mnt/c/ML/DU/local_rag_llm/"
package_path    = project_path + "run/pkgs/"
models_path     = project_path + "models/"

data_folder         = project_path + "data/"
data_folder_aiml    = project_path + "data/aiml/"       # a subset of files for testing

collection_name     = "Gen_AI_knowledge"                # ChromaDB collection name


# # Models Available
models = {
            'nomic':"nomic_embedding",
            'llama2_7_chat':"llama-2-7b-chat",
            'llama3_8_ggml':"llama3_8b_ggml",
            'llama3_8_instruct':"Llama-3-8b-Instruct",
            'qwen2_05':"Qwen2-0.5b-instruct"
            }
