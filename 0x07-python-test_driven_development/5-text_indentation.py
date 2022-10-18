#!/usr/bin/python3
""" Function """


def text_indentation(text):
    """ Indent text """

    if type(text) is not str:
        raise TypeError("text must be a string")
    punc = '.?:'
    count = 0
    while count < len(text) and text[count] == ' ':
        count += 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in punc:
            if text[count] in punc:
                print("\n")
            count += 1
            while count < len(text) and text[count] == ' ':
                count += 1
            continue
        count += 1
