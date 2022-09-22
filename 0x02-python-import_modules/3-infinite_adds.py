#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argvec = sys.argv
    len_av = len(argvec)
    infinite_sum = 0

    if len_av > 1:
        for i in range(1, len_av):
            infinite_sum += int(argvec[i])

    print(infinite_sum)
