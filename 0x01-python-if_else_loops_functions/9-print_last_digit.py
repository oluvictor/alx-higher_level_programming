#!/usr/bin/python3
# Author: Victor Ogunshola

def print_last_digit(number):
    print("{}".format(abs(number) % 10), end="")
    return abs(number) % 10
