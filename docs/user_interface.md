## Table of Contents

 - [README](../README.md)
 - [Project Proposal](project_proposal.md)
 - [Technical Approach](technical_approach.md)
 - [Application Packages](application_packages.md) Used in this project
   - [Knowledge Documents](knowledge_documents.md)
   - [User Interface](user_interface.md)
   - [LLMs](LLMs.md)
   - [Embeddings](embedding.md)
   - [Vector Database](vectorDB.md)
   - [Other Notes](misc_notes.md)
 - [References](references.md)



# User Interface

The user interface will take the users prompts and display the model's output.  The user interface can be a simple command line interface (CLI).  It can also be a web interface.  One good example is [Streamlit](https://github.com/streamlit/streamlit). 

In this case, the streamlit application is deployed in a docker container.  The streamlit application includes additional code to manage the workflow.

