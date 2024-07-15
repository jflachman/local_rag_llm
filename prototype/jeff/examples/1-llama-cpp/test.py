from llama_cpp import Llama

# Put the location of to the GGUF model that you've download from HuggingFace here
model_path = "mistral-7b-instruct-v0.2.Q4_K_M.gguf"

# Create a llama model
model = Llama(model_path=model_path)

# Prompt creation
system_message = "You are a helpful software developer"
user_message = "What do you know about BPMN 2.0 and Imixs-Workflow?"

prompt = f"""<s>[INST] <<SYS>>
{system_message}
<</SYS>>
{user_message} [/INST]"""

# Model parameters
max_tokens = 500

# Run the model
output = model(prompt, max_tokens=max_tokens, echo=True)

# Print the model output
print(output)