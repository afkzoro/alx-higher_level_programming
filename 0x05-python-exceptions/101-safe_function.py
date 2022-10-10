#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        safe = fct(*args)
    except IndexError:
        safe = None
        sys.stderr.write("Exception: list index out of range\n")
    except ZeroDivisionError:
        safe = None
        sys.stderr.write("Exception: division by zero\n")
    return safe
