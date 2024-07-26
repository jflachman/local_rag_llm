#!/bin/bash

# Start the first process
python3 -m /app/load_docs.py &

# Start the second process
python3 -m /app/my_second_process &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?