#!/usr/bin/python3
"""
pascal triangle module
"""


def factorial(n):
    """Returns factorial
    """
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    return factorial


def pascal_triangle(n):
    """
    Returns a list of integers
    """
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
