#!/bin/bash

# Use the password from pw.txt
echo "PASSWORD:" $(cat pw.txt)

# Run the script and pass flag.txt.en as an argument with the -d flag to decrypt it.
python3 ende.py -d flag.txt.en