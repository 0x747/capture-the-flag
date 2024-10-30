#!/bin/bash

# Use zipgrep to search a zip file. 
zipgrep "picoCTF" zipgrep "picoCTF" big-zip-files.zip

# OR 
# Unzip and use regular grep recursively
unzip big-zip-files.zip
grep -r "picoCTF" big-zip
