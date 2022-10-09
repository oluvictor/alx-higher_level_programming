#!/usr/bin/python3
import sys


def main():
    """prints the result of the addition of all arguments"""
    argc = len(sys.argv) - 1
    sum = 0
    if argc > 0:
        for i in range(1, argc + 1):
            sum += int(sys.argv[i])
    print(sum)


if __name__ == "__main__":
    """This part will only run in the terminal"""
    main()
