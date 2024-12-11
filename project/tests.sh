#!/bin/bash
#python3 ../project/test.py

#!/bin/bash

# Run pipeline.sh file
bash project/pipeline.sh

# Check if the previous command was successful
if [ $? -eq 0 ]; then
    echo "pipeline.sh ran successfully. Proceeding to run test.py..."
    
    # Run the Python script
    python project/tests.py
else
    echo "pipeline.sh encountered an error. Exiting script."
    exit 1
fi
