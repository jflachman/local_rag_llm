# Install dependencies

    pip install --upgrade huggingface_hub

    # Install dependencies for tensorflow-specific features
    # /!\ Warning: this is not equivalent to `pip install tensorflow`
    pip install 'huggingface_hub[tensorflow]'

    # Install dependencies for both torch-specific and CLI-specific features.
    pip install 'huggingface_hub[cli,torch]'

