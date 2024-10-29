import sys 

print("Press ENTER")
data = sys.stdin.readlines()

flag = ''

for ascii_code in data:
    # Strip newlines character from each code
    ascii_code = ascii_code.strip()

    # Cast each character to int and get its character representation
    flag += chr(int(ascii_code))

print(flag)