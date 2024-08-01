# Langchain dependencies
from langchain.document_loaders.pdf import PyPDFDirectoryLoader # Importing PDF loader from Langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter # Importing text splitter from Langchain
from langchain.embeddings import OpenAIEmbeddings # Importing OpenAI embeddings from Langchain
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document # Importing Document schema from Langchain
from langchain_community.vectorstores import Chroma # Importing Chroma vector store from Langchain
from dotenv import load_dotenv # Importing dotenv to get API key from .env file
from langchain.chat_models import ChatOpenAI # Import OpenAI LLM
import os # Importing os module for operating system functionalities
import shutil # Importing shutil module for high-level file operations
import streamlit as st

# Load environment variables from a .env file
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#openai_api_key = ''

# Directory to your pdf files:
DATA_PATH = "../data"
CHROMA_PATH = "chroma"

#Setup Page Configuration for Streamlit
st.set_page_config(
    page_title = "Local RAG llm",
    layout='wide')


query_text = st.chat_input()
if not isinstance(query_text, str):
        query_text = str(query_text)


PROMPT_TEMPLATE = """
Answer the question based only on the following context:
{context}
 - -
Answer the question based on the above context: {question}
"""


# #Trying to create the input function for Streamlit 
def user_input(query_text):
    embedding = ChatOpenAI()
    new_db = Chroma.load_local('chroma_index', embedding)
    data = new_db.similarity_search(query_text)

# if not isinstance(query_text, str):
#     raise ValueError("Expected query_text to be a string.")

def query_rag(query_text):
  """
  Query a Retrieval-Augmented Generation (RAG) system using Chroma database and OpenAI.
  Args:
    - query_text (str): The text to query the RAG system with.
  Returns:
    - formatted_response (str): Formatted response including the generated text and sources.
    - response_text (str): The generated response text.
  """
  # YOU MUST - Use same embedding function as before
  embedding_function = OpenAIEmbeddings()

  # Prepare the database
  db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
  
  # Retrieving the context from the DB using similarity search
  results = db.similarity_search_with_relevance_scores(query_text, k=3)

  # Check if there are any matching results or if the relevance score is too low
  if len(results) == 0 or results[0][1] < 0.7:
    print(f"Unable to find matching results.")

  # Combine context from matching documents
  context_text = "\n\n - -\n\n".join([doc.page_content for doc, _score in results])
 
  # Create prompt template using context and query text
  prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
  prompt = prompt_template.format(context=context_text, question=query_text)
  
  # Initialize OpenAI chat model
  model = ChatOpenAI()

  # Generate response text based on the prompt
  response_text = model.predict(prompt)
 
   # Get sources of the matching documents
  sources = [doc.metadata.get("source", None) for doc, _score in results]
 
  # Format and return response including generated text and sources
  formatted_response = f"Response: {response_text}\nSources: {sources}"
  return formatted_response, response_text

# # Let's call our function we have defined
formatted_response, response_text = query_rag(query_text)
# # and finally, inspect our final response!
# print(response_text)





def main():
    st.header("Local RAG llm")
    #Make sure this is a string.
    # query_text = st.chat_input()
    # if not isinstance(query_text, str):
    #     query_text = str(query_text)

    st.write(response_text)

if __name__ == "__main__":
    load_dotenv()
    main()

