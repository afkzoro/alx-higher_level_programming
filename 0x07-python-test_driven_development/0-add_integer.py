#!/usr/bin/python3
""" Fnnction """


def add_integer(a, b=98):
    """ Add integers """
    if type(a) not in (int, float):
        raise ValueError("a must be an integer")
    if type(b) not in (int, float):
        raise ValueError("b must be an integer")

    return int(a) + int(b)
