#!/bin/bash

decoded_flag=$(echo "bDNhcm5fdGgzX3IwcDM1" | base64 -d)
echo "picoCTF{$decoded_flag}" 
