
**Prototypes Table of Contents**

0. [Prototypes Overview](../README.md)
1. [Build AIML python environment](../1-build-env/README.md)
2. [LLM Server](../2-llm-server/README.md) with CUDA support and OpenAI compliant API *(deploy target: **docker**)*
3. [Vector Database](../3-vectorDB/README.md)
4. [User Interface](../4-user-interface/README.md)
5. TBD - [RAG Workflow](../5-rag-workflow/README.md)
6. TBD - [RAG & UI integration](../6-rag-ui-integration/README.md)

---------
---------

# LlamaIndex Project trial

**NOTE:** This section probably needs one more documentation pass to insure all the steps are clear.

## Overview

1. **Start with a clean Linux distro in WSL**.  Export and import the distro.
    - if you do not have a GPU or if your applications are already compiled with CUDA support, then **skip to section 3**.
2. Install CUDA support if desired unless compiling solutions with CUDA support.  If the proper NVIdia drivers are already installed in Windows Host, then additional CUDA installations may not be needed.  Run the [Test CUDA Notebook](test_cuda.ipynb) to see if additional installs are needed.
3. NVIDIA CUDA Deep Neural Network library (cuDNN).  This also may not be needed unless compiling solutions with CUDA support.
4. **Create an AIML Linux Environment**
5. Where are large files created using WSL distros and Docker.

## 1. Install clean Linux in WSL linux distribution (distro) from Microsoft

- Check which installation distros are available:

        wsl -l -o

    Result of that command:


        The following is a list of valid distributions that can be installed.
        Install using 'wsl.exe --install <Distro>'.

        NAME                                   FRIENDLY NAME
        Ubuntu                                 Ubuntu
        Debian                                 Debian GNU/Linux
        kali-linux                             Kali Linux Rolling
        Ubuntu-18.04                           Ubuntu 18.04 LTS
        Ubuntu-20.04                           Ubuntu 20.04 LTS
        Ubuntu-22.04                           Ubuntu 22.04 LTS
        Ubuntu-24.04                           Ubuntu 24.04 LTS
        OracleLinux_7_9                        Oracle Linux 7.9
        OracleLinux_8_7                        Oracle Linux 8.7
        OracleLinux_9_1                        Oracle Linux 9.1
        openSUSE-Leap-15.5                     openSUSE Leap 15.5
        SUSE-Linux-Enterprise-Server-15-SP4    SUSE Linux Enterprise Server 15 SP4
        SUSE-Linux-Enterprise-15-SP5           SUSE Linux Enterprise 15 SP5
        openSUSE-Tumbleweed                    openSUSE Tumbleweed


## 2. Export clean install as a backup.



Note:  This assumes that you archived a clean ubunto installation. I save mine in `C:\mywsl` and it may be accessed via `/mywsl`

`wsl --export ubuntu-22.04 /mywsl/exports/ubuntu-clean/ubuntu-22.04.tar`

Archive a clean ubunto installation

    wsl --export ubuntu-22.04 /mywsl/exports/ubuntu-clean/ubuntu-22.04.tar

Archive updates to ubuntu aiml installation

    wsl --export ubuntu-22.04-aiml /mywsl/exports/ubuntu-clean/ubuntu-22.04-aiml.tar

Install a clean ubunto installation from archive

1. delete current installation

    `wsl --unregister ubuntu-22.04-aiml`

2. install new clean ubunto from archive

    `wsl --import ubuntu-22.04-aiml /mywsl/instances/ubuntu-22.04-aiml /mywsl/exports/ubuntu-clean/ubuntu-22.04.tar`

3. check version of linux

    `cat /etc/os-release`

4. login into the distro with MS Terminal and set alias for python

    - add the following line to ~/.bashrc with nano (see edit /etc/wsl.conf below for example)

        `alias python=python3`
    - **alternately** do this from the command line.
        
        `echo -e "alias python=python3" >> ~/.bashrc`

5. check version

    `python --version`

6. update default user by adding the followling lines to /etc/wsl.conf

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
  
7. copy .ssh keys

    ```
    cp -R /mnt/c/ML/DU/.ssh ~/.ssh
    chmod 700 ~/.ssh
    chmod 600 ~/.ssh/*
    chmod 644 ~/.ssh/*.pub
    ```

8. Update git information.  
 
    **Update for with your info**

    ```
    git config --global user.email "you@example.com"
    git config --global user.name "Your Name"
    ```

10. Archive a copy of the distro if desired

    1. close terminals to your distro
    2. in Powershell:
       1. `wsl --shutdown`
       2. Note:  Update distro and tar file names as desired in the following command.
          - `wsl --export ubuntu-22.04 /mywsl/exports/ubuntu-clean/ubuntu-22.04-base.tar`




## 2. Create an AIML Linux environment

Refrence: https://github.com/marklysze/LlamaIndex-RAG-WSL-CUDA

1. Install fresh distro (ubuntu-22.04)
2. Install MiniConda: https://docs.anaconda.com/miniconda/miniconda-install/

## 2.1 Environment Setup Option 1: miniconda

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
## 2.2 Environment Setup Option 2: Anaconda


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


4. If problems with installing some packages:
 
   - Comment them out until is completes.
   - For *llama-cpp-python* issues, see pip install below with link to whl file.

5. Bulk Install Python packages using pip (pip installs)

    ```
    cp /mnt/c/ML/DU/rag_llm/prototype/jeff/0-build-env/requirements.txt ~/.
    pip install -r requirement.txt
## 2.3 Environment Setup Option 3: python venv & pip installs

WSL distro size:

| Distro | Clean |  w/pip installs |
| ------ | ----- |  -------------- |
| ubuntu 22.04 aiml | 1.921 GB | |
| ubuntu 24.04 aiml | 1.727 GB | |


1. Install Base Linux Environment (apt installs)

    1. See section "*0. Install clean Linux in WSL*" above

    2. Install linux packages:

```
        sudo apt-get update
        sudo apt update
        sudo apt upgrade
        sudo apt install pip
        sudo apt install python3-venv
```

OBE: xargs sudo apt-get install -y < requirements-apt.txt


1. Create a virtual environment

   - Notes: https://docs.python.org/3/tutorial/venv.html


    - create environment

        `python -m venv ~/llm-env`

    - activate environment

        `source ~/llm-env/bin/activate`

    - to have this environment set whenever opening a terminal, add the line to your `~/.bashrc`
         - use nano to edit ~/.bashrc
           - add `source ~/llm-env/bin/activate` to the ~/.bashrc
         - **alternately** do this from the command line.
           - `echo -e "source ~/llm-env/bin/activate" >> ~/.bashrc`

2. Install Python packages using pip (pip installs)

    ```
    cp /mnt/c/ML/DU/rag_llm/prototype/jeff/0-build-env/requirements.txt ~/.
    pip install -r requirements.txt
    ```

3. Install *llama-cpp-python*.  

    find the cuda version

    `nvidia-smi`

    use the whl file that cooresponds to the cuda version.  i.e. cu123 for Cuda 12.3

    ```
    pip install --no-cache-dir llama-cpp-python==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu123

    pip install --no-cache-dir llama-index-llms-llama-cpp==0.2.77 --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cu123

    ```

    For more info on *llama-cpp-python* and *llama-index-llms-llama-cpp* whl files, see: https://github.com/abetlen/llama-cpp-python/releases/tag/v0.2.82-cu124

4. To update all pip packages

    1. install pip-review

        `pip install pip-review`

    2. Option 1: Upgrade the packages interactively


        `pip-review --local --interactive`

    3. Option 2: Upgrade the packages interactively

        `pip-review --local --auto`

## 2.4 Install Many packages at once (Optional)


If you want to install many packages at once.  Create a `requirements.txt` file.  The name of the file is arbitrary.  However, `requirements.txt` is the standard everyone uses.  Then simply list all the packages you want to install.  You may comment out any packages you don't want to install.  The requirements.txt file in this folder is an example. To install all the listed packages, run the following:

    pip intall -r requirements.txt


# 4.0 Cleaning up WSL

Large Files are created for WSL and Docker.
- Large WSL repos: C:\Windows\System32\lxss\tools (100GB)
- Docker: C:\Users\username\AppData\Local\Docker\wsl\data (55GB)

The following  Assumes wsl exports and instances are saved in:  `C:\mywsl`.  This allows you to monitor your instance size and recreate from a known saved checkpoint you have exported previously.

    ```
    wsl --export docker-desktop-data /mywsl/exports/docker/docker-desktop-data.tar
    wsl --export docker-desktop /mywsl/exports/docker/docker-desktop.tar

    wsl --unregister docker-desktop-data
    wsl --unregister docker-desktop

    wsl --import docker-desktop-data /mywsl/instances/docker-desktop-data /mywsl/exports/docker/docker-desktop-data.tar
    wsl --import docker-desktop /mywsl/instances/docker-desktop /mywsl/exports/docker/docker-desktop.tar
    ```

----
----
----
----
----
----

----
# Appendix
----
----
----
----
----
----

## A. Install CUDA support

### NOTE: Installing CUDA toolkit may not be required for GPU support.

The latest NVIDIA Windows GPU Driver will fully support WSL 2. With CUDA support in the driver, ***existing applications*** *(compiled elsewhere on a Linux system for the same target GPU) can run unmodified within the WSL environment*.  To compile new CUDA applications, a CUDA Toolkit for Linux x86 is needed. See [3. CUDA Support for WSL 2](https://docs.nvidia.com/cuda/wsl-user-guide/index.html#:~:text=With%20CUDA%20support%20in%20the,for%20Linux%20x86%20is%20needed.).  **I suggest installing only if you find it is necessary for your application**.

- **start here:** https://docs.nvidia.com/cuda/wsl-user-guide/index.html
- https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html
- downloads here: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network
- System Requirements - https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#system-requirements


### A.1 Install CUDA Runtime libraries


1. Download and install to CUDA runtime libraries

   - The [CUDA runtime libraries](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#meta-packages) *should be* all that is needed for CUDA support to applications. it *Installs all runtime CUDA Library packages*
   - See **cuda-libraries-xx-xx** in the table: [CUDA runtime libraries](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html#meta-packages)
   - Install information for meta-packages: https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html

   1. Download the CUDA installation:

        ```
        https://developer.download.nvidia.com/compute/cuda/12.5.1/local_installers/cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb
        ```

    2. Save the downloaded deb file in `/mywsl/installs`
    3. Run the following commands 

        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin

        sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600

        sudo dpkg -i /mnt/c/mywsl/installs/cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb
        
        sudo cp /var/cuda-repo-wsl-ubuntu-12-5-local/cuda-*-keyring.gpg /usr/share/keyrings/
        
        sudo apt-get update
        
        sudo apt-get -y install cuda-libraries-12-5
        ```

2. Check installation

   - check the CUDA version in the top right corner of the printed table from `nvidia-smi`

       `nvidia-smi`

   - if you successfully install CUDA libraries or CUDA toolkit, then run the following

       `nvcc --version`


### A.2 Install FULL CUDA Toolkit **(If Desired)**

**NOTE:** Only if you need developer level integraiton with CUDA.  Otherwise, CUDA 12.X is supported when you install your NVidia drivers in windows.  You may also chose to install only the runtime libraries (see section 1.1 above)

**Pre-install checklist**
- Verify the system has a CUDA-capable GPU.
- Verify the system is running a supported version of Linux.
- Verify the system has gcc installed.
- Verify the system has the correct kernel headers and development packages installed.
- Download the NVIDIA CUDA Toolkit.
- Handle conflicting installation methods.

0. Check which GPU is on your device:

    - **Task Manager:**  Press Ctrl + Alt + Del to open the Task Manager, then click the Performance tab. Select GPU from the left navigation pane to see the GPU name and other performance statistics.
    - Insure you have the latest driver for your gpu: https://www.nvidia.com/Download/index.aspx?lang=en-us
      - Select ***Game Ready Driver*** for the very latest features, select ***studio driver*** for more stability.

1. install gcc

    `sudo apt install build-essential`

2. check install
  
    `gcc --version`

3. Verify version of linux

    `uname -m && cat /etc/*release`

4. Check version of Kernel

    `uname -r`



5. Download and install the **FULL** CUDA Toolkit (If you need to develop with CUDA)

    - **Note:** CUDA is backward compatible.  So applicaiton compiled with older CUDA version should work with newer Nvidia Drivers.  
    - Check the CUDA version of your driver

        `nvidia-smi`

    - see: https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_network

    1. Option 1: (network installer)

        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-keyring_1.1-1_all.deb
        sudo dpkg -i cuda-keyring_1.1-1_all.deb
        sudo apt-get update
        sudo apt-get -y install cuda-toolkit-12-5
        ```

    2. Option 2 (local installdownloads local installer)

        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
        sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
        wget https://developer.download.nvidia.com/compute/cuda/12.5.1/local_installers/cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb
        sudo dpkg -i cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb
        sudo cp /var/cuda-repo-wsl-ubuntu-12-5-local/cuda-*-keyring.gpg /usr/share/keyrings/
        sudo apt-get update
        sudo apt-get -y install cuda-toolkit-12-5
        ```

    3. Option 3 (local install after manually downloading deb file)

        - I put my downloaded installs for wsl distros into `C:\mywsl\installs` which can be accessed as `/mywsl/installs`.  See this in line 3 below.

        ```
        wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
        sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
        sudo dpkg -i /mnt/c/mywsl/installs/cuda-repo-wsl-ubuntu-12-5-local_12.5.1-1_amd64.deb
        sudo cp /var/cuda-repo-wsl-ubuntu-12-5-local/cuda-*-keyring.gpg /usr/share/keyrings/
        sudo apt-get update
        sudo apt-get -y install cuda-toolkit-12-5
        ```

    4. Option 4 (using nvidia-cuda-toolkit)

       - Note: This method may install an older version of the cuda toolkit.  On 7/24 it installed Cuda v11.5.119 when Options 1-3 above installed 12.5.1.

        ```
        sudo apt-get install nvidia-cuda-toolkit
        ```

6. Check installation

- check the CUDA version in the top right corner of the printed table from `nvidia-smi`

    `nvidia-smi`

- if you successfully install CUDA libraries or CUDA toolkit, then run the following

    `nvcc --version`

## B. NVIDIA CUDA Deep Neural Network library (cuDNN) **(If Desired)**

You should only need to install the runtime package (see packages below) if you are not compiling an application with cuDNN support.

- https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html
- Packages:  https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html#base-packages
- Install cuDNN from pip: https://docs.nvidia.com/deeplearning/cudnn/latest/installation/linux.html#installing-cudnn-with-pip
- Not needed if installing from pip
  - Downloads: https://developer.nvidia.com/rdp/cudnn-archive
  - Note:  Based the packages, `libcudnn9-cuda-12` Installs the ***runtime package*** which contains the latest available cuDNN 9 dynamic libraries for the latest available CUDA 12 version.

    ```
    python3 -m pip install nvidia-cudnn-cu12
    ```

----
----
----
----
----


## Old Notes

- youtube
    - https://www.youtube.com/watch?v=f-AXdiCyiT8
    - https://www.youtube.com/watch?v=hH4WkgILUD4
- github
    - https://github.com/krishnaik06/Llamindex-Projects/tree/main/Basic%20Rag
    - https://github.com/marklysze/LlamaIndex-RAG-WSL-CUDA

Installs

```
pip install nvidia-pyindex
pip install nvidia-cublas

pip install llama-index-embeddings-huggingface
pip install llama-index-llms-llama-cpp
pip install llama-index
```

