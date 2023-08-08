"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def fibonacci_iterative(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def fibonacci_recursive(n):
    pass


print(fibonacci_iterative(6))
print(fibonacci_recursive(6))