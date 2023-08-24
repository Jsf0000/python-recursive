"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

import sys
sys.path.append("..")  # Adds higher directory to python modules path.

from trace_recursion import trace




def gcd_recursive(a, b):
    if b == 0:
        #base case
        return a
    else:
        # recursive case
        return gcd_recursive(b, a % b)




gcd_recursive = trace(gcd_recursive)
print(gcd_recursive(32, 12))  # From slides
print(gcd_recursive(50, 15))
print(gcd_recursive(42, 28))
print(gcd_recursive(28, 42))
print(gcd_recursive(345, 766))  # Co-prime
