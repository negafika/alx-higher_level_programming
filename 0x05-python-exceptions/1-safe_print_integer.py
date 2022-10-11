#!/usr/bin/python3
def safe_print_integer(value):
    ind = True
    try:
        num = int(value)
        print("{:d}".format(num))
    except ValueError:
        ind = False
    return ind
