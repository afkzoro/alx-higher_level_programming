#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    """

    Prints the result of the sum of parameters a and b

    """
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
