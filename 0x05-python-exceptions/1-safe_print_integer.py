#!/usr/bin/python3
def safe_print_integer(value):
    ind = True
    try:
        print("{:d}".format(value))
    except ValueError:
        ind = False
    return ind
