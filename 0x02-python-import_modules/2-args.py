#!/usr/bin/python3
import sys

def main():
    argc = len(sys.argv) - 1
    arg_str = "argument" if argc == 1 else "arguments"
    punctuation = "." if argc == 0 else ":"
    print("{} {}{}".format(argc, arg_str, punctuation))
    if argc > 0:
        for i in range(1, argc + 1):
            print("{}: {}".format(i, sys.argv[i]))
if __name__ == "__main__":
    """This part will only run in the terminal"""
    main()
