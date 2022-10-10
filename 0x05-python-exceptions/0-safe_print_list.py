#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    new_list = []
    try:
        for i in range(0, x):
            new_list.append(my_list[i])
    except IndexError:
        new = [str(int) for int in new_list]
        return "".join(new)

    new = [str(int) for int in new_list]
    return "".join(new)
