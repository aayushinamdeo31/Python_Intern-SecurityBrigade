# Task 8

# Please write a program to compress and decompress the string
# "Music industry hails passage of the Music Modernization Act".

import binascii
import random
import string
import zlib, gzip


def str_to_hex(str):
    return binascii.hexlify(str)  # Return the hexadecimal representation of the binary data


def hex_to_str(hex):
    return binascii.unhexlify(hex)  # Return the binary data represented by the hexadecimal string


def main():

    sentence = "Music industry hails passage of the Music Modernization Act"
    print('String is - ', sentence)
    print()
    # Compressing string
    str_comp = zlib.compress(sentence.encode('utf-8'))
    print('Compressed String is - ', str_comp)
    print()
    str_comp = str_to_hex(str_comp)
    # Decompressing string
    unhex_str = hex_to_str(str_comp)

    if 'x' in str(unhex_str):
        unhex_str = zlib.decompress(unhex_str).decode('utf8')

    print('Decompressed String is - ', unhex_str)
    print("---" * 20)


if __name__ == '__main__':
    print("---" * 20)
    main()
