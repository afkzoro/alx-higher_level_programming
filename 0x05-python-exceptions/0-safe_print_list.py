#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = ""
    try:
        for i in range(0, x):
            num += str(my_list[i])
    except IndexError:
        return int(num)
    return int(num)
