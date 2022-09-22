#!/usr/bin/python3
from calculator_1.py import add, sub, mul, div
if __name__ == "__main__":
    from sys import argv
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    elif argv[1] not in ['+','-','*','/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        if argv[1] == '+':
            print('{:d} + {:d} = {:d}'.format(argv[0], argv[2],add(argv[0],argv[2])))
        elif argv[1] == '-':
            print('{:d} - {:d} = {:d}'.format(argv[0], argv[2],sub(argv[0],argv[2])))
        elif argv[1] == '*':
            print('{:d} * {:d} = {:d}'.format(argv[0], argv[2], mul(argv[0],argv[2])))
        else:
            print('{:d} / {:d} = {:d}'.format(argv[0],argv[2],div(argv[0],argv[2])))
