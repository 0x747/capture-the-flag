#!/bin/bash

# Alternatively use CyberChef to decode the string twice and bruteforce Caesar Cipher.

b64decoded=$(cat enc_flag | base64 -d)
b64decoded=$(echo ${b64decoded:2:-1} | base64 -d)

python3 caesar_decrypt.py $b64decoded