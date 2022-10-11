#!/usr/bin/python3
"""_summary_

    Raises:
        TypeError: _description_
        ValueError: _description_
        TypeError: _description_
        ValueError: _description_

    Returns:
        _type_: _description_
    """


class Square:
    """_summary_
    """
    def __init__(self, size=0, position=(0, 0)):
        """_summary_

        Args:
            size (int, optional): _description_. Defaults to 0.

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.size = size
        self.position = position

    @property
    def size(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size

    @size.setter
    def size(self, size):
        """_summary_

        Args:
            size (_type_): _description_

        Raises:
            TypeError: _description_
            ValueError: _description_
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.__size ** 2

    @property
    def position(self):
        return self.__positon

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or
                len(value) != 2 or
                all(isinstance(num, int) is False for num in value) or
                all(num >= 0 for num in value)) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if self.__size == 0:
            print("")
            return None

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
