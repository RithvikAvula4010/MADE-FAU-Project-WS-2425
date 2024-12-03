#!/bin/bash

# Run pipeline.sh file
# pipeline was created in Jayvee. Data Extraction taking too much time to extract the data (approx 20 to 30 min), hence do not execute the pipeline.

bash ../project/pipeline.sh

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "pipeline.sh ran successfully. Proceeding to run tests.py..."
    
    # Run the Python script
    python ../project/tests.py
else
    echo "pipeline.sh encountered an error. Exiting script."
    exit 1
fi
