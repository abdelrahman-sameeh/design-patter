#!/bin/bash

# Check if the file argument is provided
if [ -z "$1" ]; then
    echo "Error: Enter File Name To Run"
    exit 1
fi

# Check if the provided file exists
if [ ! -f "$1" ]; then
    echo "Error: File '$1' not found."
    exit 1
fi

# Run the Python file
python3 "$1"