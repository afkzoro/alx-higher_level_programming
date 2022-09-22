#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """
    Prints the number and list of arguments

    """
    arg_vec = sys.argv
    len_av = len(arg_vec) - 1

    if len_av > 1:
        print(len_av, 'arguments:')
        for i in range(1, len_av + 1):
            print('{:d}: {}'.format(i, arg_vec[i]))
    elif len_av == 1:
        print(len_av, 'argument:')
        for i in range(1, len_av + 1):
            print('{:d}: {}'.format(i, arg_vec[i]))
    elif len_av == 0:
        print(len_av, 'arguments.')
