#!/usr/bin/python3
# Author: Victor Ogunshola

i = 0
for alphabet in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(alphabet - i)), end="")
    i = 32 if i == 0 else 0
