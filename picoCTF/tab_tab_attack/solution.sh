#!/bin/bash

unzip Addadshashanammu.zip

# grep will return the path of the binary file containing the flag. 
./$(grep -l -r "picoCTF" Addadshashanammu)