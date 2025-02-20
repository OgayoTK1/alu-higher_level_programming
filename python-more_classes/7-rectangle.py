#!/usr/bin/python3
"""
This module defines a Rectangle class with width and height attributes,
methods to calculate area and perimeter, a custom string representation,
an eval-compatible repr representation, a deletion message, and class
attributes to track the number of instances and the print symbol.
"""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    # Class attributes to track instances and the print symbol
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        "Return string representation of rectangle withprint_symbol characters"
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join([symbol * self.__width for _ in range(self.__height)])

    def __repr__(self):
        "Return a string representation to recreate a new instance usingeval()"
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        "Print amessage when an instance of Rectangle is deleted and decrement"
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement instance count
