#!/bin/bash

# # Check if a config file argument is provided
# if [ -n "$1" ]; then
#     CONFIG_FILE="--config_file $1"
# else
#     CONFIG_FILE=""
# fi

# Use the PORT environment variable or default to 11434
PORT=${PORT:-11434}
SERVER=${SERVER:""}

# Run the server with the config file argument if provided
#exec python3 -m llama_cpp.server $CONFIG_FILE --port $PORT
exec python3 -m llama_cpp.server $SERVER --port $PORT