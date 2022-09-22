#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    length = len(argv)
    if length == 1:
        print('{:d} argument:'.format(length))
    elif length == 0:
        print('{:d} arguments.'.format(length))
    for i, each in enumerate(argv):
        print('{:d}: {:s}'.format(i, each))
