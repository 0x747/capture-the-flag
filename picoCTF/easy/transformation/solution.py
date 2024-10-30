import codecs

enc_flag = open("enc").read()
hex_flag = ''
flag = ''
for c in enc_flag:
    hex_flag += hex(ord(c)).lstrip("0x")  
    
# for i in range(0, len(hex_flag), 2):
#     flag += chr(int(hex_flag[i:i+2], 16))

flag += ''.join([chr(int(hex_flag[i:i+2], 16)) for i in range(0, len(hex_flag), 2)])

print(flag)
