#!/usr/bin/python3
"""
This module defines a BaseGeometry class with integer validation.
"""

class BaseGeometry:
    """A class with basic geometry functions."""

    def area(self):
        """Raises an Exception with a message since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If `value` is not an integer.
            ValueError: If `value` is <= 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

