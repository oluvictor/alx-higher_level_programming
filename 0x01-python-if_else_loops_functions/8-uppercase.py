#!/usr/bin/python3
# Author - Victor Ogunshola

def uppercase(str):
    """Print a string in uppercase."""
    new_str = ''
    for c in str:
        c_ascii = ord(c)
        if c_ascii >= 97 and c_ascii <= 122:
            new_str = new_str + chr(c_ascii - 32)
        else:
            new_str = new_str + chr(c_ascii)
    print(new_str)
