#!/bin/bash

exiftool ukn_reality.jpg | grep "Attribution URL" | awk '{print $4}' | base64 -d