#!/bin/bash

# Similar to Can You See

exiftool cat.jpg | grep "License" | awk '{print $3}' | base64 -d