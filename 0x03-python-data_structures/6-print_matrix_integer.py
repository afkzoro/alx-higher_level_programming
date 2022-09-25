#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for elements in i:
            print('{}'.format(elements), end=' ')
        print('')
