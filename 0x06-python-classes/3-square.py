#!/usr/bin/python3
"""_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """


class Square:
    """_summary_
    """
    def __init__(self, size=0):
        """ Init method """
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """ Area method """
        return self.__size * self.__size
