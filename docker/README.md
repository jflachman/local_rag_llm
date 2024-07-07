# Build application docker image

## Build streamlit + application code.

See:  https://docs.streamlit.io/deploy/tutorials/docker

`docker build -f Dockerfile-streamlit -t streamlit .`

### Modify Streamlit to add additional application code.

**Clone Streamlit example**

`git clone git@github.com:streamlit/streamlit-example.git`

**modify** 

modify streamlit_app.py and requirements.txt to build out the rest of the application

## Run streamlit container

`docker run -it -d -p 8501:8501 streamlit`

with local file system:

`docker run -it -d -v /path/to/file/:/app -p 8501:8501 streamlit`