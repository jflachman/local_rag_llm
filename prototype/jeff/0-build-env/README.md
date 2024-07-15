
# LlamaIndex Project trial

## 0. Install clean Linux in WSL

Note:  This assumes that you archived a clean ubunto installation where /mywsl is C:\mywsl

`wsl --export ubuntu-22.04 /mywsl/exports/ubuntu-clean/ubuntu-22.04.tar`


Install a clean ubunto installation from archive
- delete current installation

    `wsl --unregister ubuntu-22.04-aiml`

- install new clean ubunto from archive

    `wsl --import ubuntu-22.04-aiml /mywsl/instances/ubuntu-22.04-aiml /mywsl/exports/ubuntu-clean/ubuntu-22.04.tar`

- login into the distro with MS Terminal and set alias for python

    `alias python=python3`

- check version

    `python --version`

- update default user by adding the followling lines to /etc/wsl.conf

    ```
    [user]
    default=username
    ```

    - *username* is the username you created when installing ubuntu on wsl

  - use nano

      ```
      nano /etc/wsl.conf
      ```

      - use arrow keys to make navigate in nano
      - ^X to exit
      - Y to save
      - confirm same file name "wsl.conf"

- copy .ssh keys

    ```
    cp -R /mnt/c/ML/DU/.ssh ~/.ssh
    ```

## 1. Create 

Refrence: https://github.com/marklysze/LlamaIndex-RAG-WSL-CUDA

1. Install fresh distro (ubuntu-22.04)
2. Install MiniConda: https://docs.anaconda.com/miniconda/miniconda-install/

## 1.1 Environment Setup Option 1: miniconda

1. Install miniconda
    ```
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
    ```

2. Initialize miniconda

    ```
        ~/miniconda3/bin/conda init bash
        ~/miniconda3/bin/conda init zsh
    ```

3. Create Env and activate

- https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

    ```
    conda create --name <my-env>
    <or in our case>
    conda env create -f environment.yml

    conda activatge ragllm
    ```

Note:  Remove a conda environment:  `conda remove -n ragllm --all`
## 1.2 Environment Setup Option 2: Anaconda


`https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh`


1. Install anaconda
    ```
    mkdir -p ~/anaconda3
    wget https://repo.anaconda.com/archive/Anaconda3-2024.06-1-Linux-x86_64.sh -O ~/anaconda3/anaconda.sh
    bash ~/anaconda3/anaconda.sh -b -u -p ~/anaconda3
    rm -rf ~/anaconda3/anaconda.sh
    ```

2. Initialize anaconda

    ```
        ~/anaconda3/bin/conda init bash
        ~/anaconda3/bin/conda init zsh
    ```

3. Create Env and activate

- https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html

    ```
    conda create --name <my-env>
    <or in our case>
    conda env create -f environment.yml

    conda activate ragllm
    ```

## 1.3 Environment Setup Option 3: python venv & pip installs

1. Install Base Linux Environment

    1. See section "*0. Install clean Linux in WSL*" above

    2. Install linux packages:

        `xargs sudo apt-get -y install < requirements-apt.txt`

2. Create a virtual environment

   - Notes: https://docs.python.org/3/tutorial/venv.html

    - create environment

        `python -m venv llm-env`

    - activate environment

        `source llm-env/bin/activate`


3. Install Python packages using pip

```
pip install -r requirements-pip.txt

pip install --no-cache-dir llama-cpp-python==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu123

pip install --no-cache-dir llama-index-llms-llama-cpp==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu123

```


# 2.0 Cleaning up WSL

Large Files
- Large WSL repos: C:\Windows\System32\lxss\tools (100GB)
- Docker: C:\Users\username\AppData\Local\Docker\wsl\data (55GB)

    ```
    wsl --export docker-desktop-data /mywsl/exports/docker/docker-desktop-data.tar
    wsl --export docker-desktop /mywsl/exports/docker/docker-desktop.tar

    wsl --unregister docker-desktop-data
    wsl --unregister docker-desktop

    wsl --import docker-desktop-data /mywsl/instances/docker-desktop-data /mywsl/exports/docker/docker-desktop-data.tar
    wsl --import docker-desktop /mywsl/instances/docker-desktop /mywsl/exports/docker/docker-desktop.tar
    ```

## Old

- youtube
    - https://www.youtube.com/watch?v=f-AXdiCyiT8
    - https://www.youtube.com/watch?v=hH4WkgILUD4
- github
    - https://github.com/krishnaik06/Llamindex-Projects/tree/main/Basic%20Rag
    - https://github.com/marklysze/LlamaIndex-RAG-WSL-CUDA

Installs

pip install nvidia-pyindex
pip install nvidia-cublas

pip install llama-index-embeddings-huggingface
pip install llama-index-llms-llama-cpp
pip install llama-index

# new install

pip install llama-cpp-agent

pip install --no-cache-dir llama-cpp-python==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu124





    `wsl --import du-aiml /mywsl/instances/du-aiml_orig /mywsl/exports/du-aiml_original/du-aiml_original.tar`