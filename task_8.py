# Task 8

# Please write a program to compress and decompress the string "Music industry hails passage of the Music Modernization Act".

import binascii
import random
import string
import zlib,gzip

def str_to_hex(s):
    return binascii.hexlify(s)  # Return the hexadecimal representation of the binary data

def hex_to_str(h):
    return binascii.unhexlify(h)  # Return the binary data represented by the hexadecimal string


def main():
    string = "Music industry hails passage of the Music Modernization Act"
    print('String is - ',string)
    print()
    
    # Compressing string
    string_comp = zlib.compress(string.encode('utf-8'))
    print('Compressed String is - ',string_comp)
    print()
    string_comp = str_to_hex(string_comp)

    # Decompressing string
    unhex_string = hex_to_str(string_comp)
    if 'x' in str(unhex_string):
        unhex_string = zlib.decompress(unhex_string).decode('utf8')
    print('Decompressed String is - ',unhex_string)
    print("---"*20)


if __name__ == '__main__':
    print("---"*20)
    main()
