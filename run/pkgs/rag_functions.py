import os
from langchain_community.document_loaders import PyMuPDFLoader
import pymupdf4llm
from langchain.text_splitter import MarkdownTextSplitter
import pickle

# *******************************************************************
# Function Summary
# *******************************************************************
# -------------------------------------------------------------------
# - load_imported_docs (file_list_pkl)
# ----- return imported_docs
# - write_imported_docs(imported_docs, file_list_pkl)
# - read_doc_directory( directory, imported_docs )
# ----- return imported_docs, documents
# - read_doc_directory_pdf_md( directory, imported_docs )
# ----- return imported_docs, documents (documents already split via markdown)
# - print_dict( dict_item, name)
# ----- None
# - print_list( list_items, name)
# ----- None
# - collection_exists(collections, collection_name)
# ----- bool
# - check_distances(distances, threshold=0.7)
# ----- bool
# - clean_and_join_doc_chunks(documents)
# ----- joined_text
# - 
# ----- 
# -------------------------------------------------------------------

# -------------------------------------------------------------------
## Manage a file that contains a list of files already read.
# -------------------------------------------------------------------
def load_imported_docs (file_list_pkl):
    if os.path.exists(file_list_pkl):
        print(f"The file {file_list_pkl} exists.")
        # Load Import Docs DB
        with open(file_list_pkl, 'rb') as file: imported_docs = pickle.load(file)
    else:
        print(f"The file {file_list_pkl} does not exist.")
        imported_docs = {}
        
    return imported_docs

def write_imported_docs(imported_docs, file_list_pkl):
    with open(file_list_pkl, 'wb') as file: pickle.dump(imported_docs, file)
    

# -------------------------------------------------------------------
# Substitute for - DirectoryLoader
# from langchain_community.document_loaders import DirectoryLoader
# -------------------------------------------------------------------
def read_doc_directory( directory, imported_docs ):
    documents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = (root + '/' + file).replace('//','/')
            if file.endswith(".pdf"):
                loader = PyMuPDFLoader(file_path)
                document = loader.load()
                documents += document
                imported_docs[ file] =  file_path
                print(f"Loaded: {file}")
            if file.endswith(".docx"):
                print(f"I don't know how to handle word docs:  file: {file_path}")
                    
    return imported_docs, documents


# -------------------------------------------------------------------
# Substitute for - DirectoryLoader
# from langchain_community.document_loaders import DirectoryLoader
# This version includes a markdown option
# -------------------------------------------------------------------
def read_doc_directory_pdf_md( directory, imported_docs ):
    documents = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = (root + '/' + file).replace('//','/')
            if file.endswith(".pdf"):
                if (markdown):
                    splitter = MarkdownTextSplitter(chunk_size=40, chunk_overlap=0)
                    md_text = pymupdf4llm.to_markdown(file_path)  # get markdown for all pages
                    document = splitter.create_documents([md_text])
                    documents += document
                    print(f"Doc: {document}")
                else:
                    loader = PyMuPDFLoader(file_path)
                    documents += loader.load()
                
                imported_docs[ file] =  file_path
                
            if file.endswith(".docx"):
                print(f"I don't know how to handle word docs:  file: {file_path}")
                    
    return imported_docs, documents

# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------
def print_dict( dict_item, name):
    print(f"\nDictionary: {name}")
    for key in dict_item.keys():
        print(f"  {key}: {dict_item[key]}")
        
# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------
def print_list( list_items, name):
    print(f"\nList: {name}")
    for i, item in enumerate(list_items):
        print(f"  {i}: {item}")
        
# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------
def collection_exists(collections, collection_name):
    for collection in collections:
        if collection.name == collection_name:
            return True
    return False

# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------
def check_distances(distances, threshold=0.7):
    if not distances or not distances[0]:
        return True  # List is empty
#    return all(score < threshold for score in distances[0])
    return any(score < threshold for score in distances[0])

# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------
def clean_and_join_doc_chunks(documents):
    # Flatten the list of lists
    flattened_docs = [item for sublist in documents for item in sublist]
    
    # Remove parts like ([18], p. 5) using regex
    # cleaned_docs = [re.sub(r'\(\[\d+\], p\. \d+\)', '', doc) for doc in flattened_docs]
    
    # # Join the cleaned documents with the specified delimiter
    # joined_text = "\n\n - -\n\n".join(cleaned_docs)
    joined_text = "\n\n - -\n\n".join(flattened_docs)
    
    return joined_text

# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# 
# -------------------------------------------------------------------

        