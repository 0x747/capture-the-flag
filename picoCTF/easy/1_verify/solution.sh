#!/bin/bash

checksum=$(cat checksum.txt);
filename=$(sha256sum  files/* | grep "$checksum" | awk '{print $2}'); 
./decrypt.sh $filename