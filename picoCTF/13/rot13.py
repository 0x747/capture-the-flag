import codecs
import sys

encoded_flag = sys.argv[1]

print(codecs.decode(encoded_flag, 'rot13'))

