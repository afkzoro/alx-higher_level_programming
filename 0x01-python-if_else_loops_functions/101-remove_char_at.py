#!/usr/bin/python3
def remove_char_at(str, n):
    new_word = ""

    for i in range(len(str)):
        if i != n:
            new_word += str[i]

    return new_word
