#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, encoding='utf-8') as fp:
        return fp.write(text)
