#!/bin/bash

# Name: test.sh
# Description: Script to run unit tests for the data pipeline

# Exit immediately if a command exits with a non-zero status
set -e

# Ensure all dependencies are installed
echo "Installing required dependencies..."
pip install -r requirements.txt > /dev/null 2>&1 || pip install pandas requests

# Run the test suite using unittest
echo "Running unit tests..."
python -m unittest discover -s . -p "test.py"

# Check the exit status of the tests
if [ $? -eq 0 ]; then
    echo "All tests passed successfully!"
else
    echo "Some tests failed. Please check the output above."
    exit 1
fi
