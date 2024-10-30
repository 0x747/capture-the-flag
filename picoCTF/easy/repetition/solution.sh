#!/bin/bash

encodedFlag=$(cat enc_flag)

decode_base64() {

    encoded="$1"
    
    if [[ "$encoded" == *"picoCTF" ]]; then
        echo "$encoded"
    fi 
    
    decode_base64 $(echo "$encoded" | base64 -d)
}

decode_base64 "$(cat enc_flag)"