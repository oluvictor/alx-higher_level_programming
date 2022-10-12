#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    argc = len(sys.argv) - 1
    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operator = sys.argv[2]
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if operator not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, operator, b, ops[operator](a, b)))


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
