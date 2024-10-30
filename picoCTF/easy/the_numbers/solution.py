import sys

# Enter the numbers separated by spaces
# python3 solution.py "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"

encoded_flag = sys.argv[1].split(' ')
print(encoded_flag)
flag = ''

for c in encoded_flag:
    if c.isnumeric():
        flag += chr(65 + int(c) - 1)
        continue
    flag += c

print(flag)