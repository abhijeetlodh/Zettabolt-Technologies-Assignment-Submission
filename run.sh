#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run the main script and log output
python main.py > output.log 2>&1