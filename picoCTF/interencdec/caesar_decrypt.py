import sys

ciphertext = sys.argv[1]

def caesar_decrypt(cipher_text: str, shift: int) -> str:
    plain_text = "" 

    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            plain_text += char
            
    return plain_text

for shift in range(1, 26):
    flag = caesar_decrypt(ciphertext, shift)
    
    if 'picoCTF' in flag:
        print(flag)


