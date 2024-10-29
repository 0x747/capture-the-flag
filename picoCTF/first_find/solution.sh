#!/bin/bash

# Unzip files.zip
unzip files.zip
# Use find command to find the uber-secret.txt and cat the file contents
cat $(find files/ -name "uber-secret.txt")