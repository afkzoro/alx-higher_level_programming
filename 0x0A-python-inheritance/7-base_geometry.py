#!/usr/bin/python3
""" Base Geometry """


class BaseGeometry:
    """ A class """
    def area(self):
        """ Calculates Area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ checks type """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
