# Langchain dependencies
from langchain.document_loaders.pdf import PyPDFDirectoryLoader # Importing PDF loader from Langchain
from langchain.text_splitter import RecursiveCharacterTextSplitter # Importing text splitter from Langchain
from langchain.embeddings import OpenAIEmbeddings # Importing OpenAI embeddings from Langchain
from langchain.prompts import ChatPromptTemplate
from langchain.schema import Document # Importing Document schema from Langchain
from langchain.vectorstores.chroma import Chroma # Importing Chroma vector store from Langchain
from dotenv import load_dotenv # Importing dotenv to get API key from .env file
from langchain.chat_models import ChatOpenAI # Import OpenAI LLM
import chromadb

import os # Importing os module for operating system functionalities
import shutil # Importing shutil module for high-level file operations

# Directory to your pdf files:
DATA_PATH = "../data"
CHROMA_PATH = "chroma"

def load_documents():
  """
  Load PDF documents from the specified directory using PyPDFDirectoryLoader.
  Returns:
  List of Document objects: Loaded PDF documents represented as Langchain
                                                          Document objects.
  """
  # Initialize PDF loader with specified directory
  document_loader = PyPDFDirectoryLoader(DATA_PATH) 
  # Load PDF documents and return them as a list of Document objects
  return document_loader.load() 

def split_text(documents: list[Document]):
  """
  Split the text content of the given list of Document objects into smaller chunks.
  Args:
    documents (list[Document]): List of Document objects containing text content to split.
  Returns:
    list[Document]: List of Document objects representing the split text chunks.
  """
  # Initialize text splitter with specified parameters
  text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, # Size of each chunk in characters
    chunk_overlap=100, # Overlap between consecutive chunks
    length_function=len, # Function to compute the length of the text
    add_start_index=True, # Flag to add start index to each chunk
  )

  # Split documents into smaller chunks using text splitter
  chunks = text_splitter.split_documents(documents)
  print(f"Split {len(documents)} documents into {len(chunks)} chunks.")

  # Print example of page content and metadata for a chunk
  document = chunks[0]
  print(document.page_content)
  print(document.metadata)

  return chunks # Return the list of split text chunks

def collection_exists(collections, collection_name):
    for collection in collections:
        if collection.name == collection_name:
            return True
    return False

from chromadb.utils import embedding_functions

# Use a different sentence transformer: all-mpnet-base-v2
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

# Get a chromadb client
client = chromadb.HttpClient(host='localhost', port=8200)

# Create the collection
collection_name = "local_kb"

# Get list of collections
collections = client.list_collections()

# Determine if collection already exist
exists = collection_exists(collections, collection_name)

# Clear and create collection
if exists:
    # Delete and Recreate
    client.delete_collection(name=collection_name)
    chroma_collection = client.create_collection(
                        name=collection_name, 
                        embedding_function=sentence_transformer_ef)
else:
    chroma_collection = client.create_collection(
                        name=collection_name, 
                        embedding_function=sentence_transformer_ef)
    
# Load all the documents and create document structure
documents = load_documents() # Call the function

# Split documents into chunks
chunks = split_text(documents)

document = chunks[4]

print(document)
print(f"\n{document.page_content}")
print(f"\n{document.metadata}")

len(chunks)

metadata_list = []
content_list = []
id_list = []
for i, document in enumerate(chunks):
    content     = chunks[i].page_content
    file_path   = chunks[i].metadata['source']
    page        = chunks[i].metadata['page']
    index       = chunks[i].metadata['start_index']
    
    file_parts  = file_path.split('/')
    filename = file_parts[len(file_parts)-1]
    
    chunks[i].metadata['filename'] = filename
    
    id = filename + "_" + str(page) + "_" + str(index)
    
    content_list.append(content)
    metadata_list.append(chunks[i].metadata)
    id_list.append(id)

chroma_collection.add(
    documents=content_list,
    metadatas=metadata_list,
    ids=id_list
)

collection_len = chroma_collection.count()
collection_list = chroma_collection.peek()

print(collection_len)

print(collection_list)

results = chroma_collection.query(
    query_texts=[
        "This is a query about machine learning and data science"
    ],
    n_results=3
)

print(results)

def print_dict( dict_item, name):
    print(f"\nDictionary: {name}")
    for key in dict_item.keys():
        print(f"  {key}: {dict_item[key]}")
        
def print_list( list_items, name):
    print(f"\nList: {name}")
    for i, item in enumerate(list_items):
        print(f"  {i}: {item}")


print_dict(results, 'results')