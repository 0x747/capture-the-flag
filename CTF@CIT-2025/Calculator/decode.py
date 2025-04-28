with open("tabs_and_spaces.txt", 'r') as f:
    content = f.readlines()

flag = ''

for word in content:
    binary = ''
    for char in word:
        if char == ' ':
            binary += '0'
        elif char == '\t':
            binary += '1'
        elif char == '\n':
            binary += ' '
            
    ascii_code = int(binary, 2)
    flag += chr(ascii_code) if ascii_code > 1 else '' 

print("Flag:", flag)