#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit 1
    operator = sys.argv[2]
    a = sys.argv[1]
    b = sys.argv[3]
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
