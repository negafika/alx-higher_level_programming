#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        ind = True
    except BaseException:
        ind = False
    return ind
