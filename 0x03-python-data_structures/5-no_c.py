#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if i != 67 and i != 99:
            print('{:d}'.format(my_string[i]))
