

# Debugging Docker

## My issue requiring the need to debug docker

I had an issue with the llama-cpp-server and needed to debug.  

    Traceback (most recent call last):
    File "/usr/lib/python3.10/runpy.py", line 196, in _run_module_as_main
        return _run_code(code, main_globals, None,
    File "/usr/lib/python3.10/runpy.py", line 86, in _run_code
        exec(code, run_globals)
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/__main__.py", line 97, in <module>
        main()
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/__main__.py", line 83, in main
        app = create_app(
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/app.py", line 150, in create_app
        set_llama_proxy(model_settings=model_settings)
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/app.py", line 70, in set_llama_proxy
        _llama_proxy = LlamaProxy(models=model_settings)
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/model.py", line 31, in __init__
        self._current_model = self.load_llama_from_model_settings(
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/server/model.py", line 222, in load_llama_from_model_settings
        _model = create_fn(
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/llama.py", line 354, in __init__
        raise ValueError(f"Model path does not exist: {model_path}")
    ValueError: Model path does not exist: /models/qwen2_500m/qwen2-0_5b-instruct-q5_k_m.gguf
    Exception ignored in: <function Llama.__del__ at 0x7fc9c1628b80>
    Traceback (most recent call last):
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/llama.py", line 1972, in __del__
        self.close()
    File "/usr/local/lib/python3.10/dist-packages/llama_cpp/llama.py", line 1969, in close
        self._stack.close()
    AttributeError: 'Llama' object has no attribute '_stack'

## What I did to investigate


















# Reference:

**Query** I asked CoPilot how to debug a docker container.

**CoPilot Response**

Debugging a script manually inside a Docker container can be quite effective. Here are some steps and tips to help you debug your script:

**1. Start an Interactive Shell in the Container**

First, run an interactive shell in your Docker container:

    docker run -it --entrypoint /bin/bash your-docker-image

This command will start a bash shell inside the container, allowing you to interact with the filesystem and run commands manually.

**2. Install Debugging Tools**

If your container doesn’t have debugging tools installed, you can add them. For example, you might want to install vim, nano, or htop:

    apt-get update
    apt-get install -y vim nano htop

**3. Run Your Script Manually**

Navigate to the directory containing your script and run it:

    cd /path/to/your/script
    python your_script.py

Observe the output and any error messages that appear.

**4. Use Print Statements**

Add print statements to your script to output variable values and checkpoints. This can help you understand the flow of your script and identify where it might be failing.

**5. Use a Debugger**

For Python scripts, you can use the built-in pdb debugger. Insert the following line at the point where you want to start debugging:

Python: `AI-generated code. Review and use carefully.`

    import pdb; pdb.set_trace()

When the script reaches this line, it will pause and allow you to inspect variables and step through the code.

**6. Check Logs**

If your application generates logs, check them for any error messages or warnings. Logs can provide valuable insights into what might be going wrong.

**7. Use VS Code for Remote Debugging**

You can also use Visual Studio Code to attach a debugger to your running container. Here’s a brief overview:

1. **Install the Remote - Containers extension** in VS Code.
2. **Attach to the running container** using the command palette (Ctrl+Shift+P > Remote-Containers: Attach to Running Container).
3. **Set up a launch configuration** in launch.json to attach the debugger to your script.

**Example `launch.json` for Python:** `AI-generated code. Review and use carefully.`

JSON

    {
    "version": "0.2.0",
    "configurations": [
        {
        "name": "Python: Remote Attach",
        "type": "python",
        "request": "attach",
        "connect": {
            "host": "localhost",
            "port": 5678
        },
        "pathMappings": [
            {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/app"
            }
        ]
        }
    ]
    }


Add the following lines to your script to enable remote debugging:  `AI-generated code. Review and use carefully.`

Python

    import debugpy
    debugpy.listen(("0.0.0.0", 5678))
    print("Waiting for debugger to attach...")
    debugpy.wait_for_client()


**8. Use Docker Debug Command**

Docker also provides a docker debug command that can help you get a shell into any container or image, even if they don’t contain a shell1.

By following these steps, you should be able to effectively debug your script inside a Docker container. 😊