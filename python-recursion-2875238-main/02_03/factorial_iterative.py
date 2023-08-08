"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


# def factorial_iterative_while(n):  # Condition-controlled version
#     pass
#
#
# # Let's do some basic testing
# assert factorial_iterative_while(4) == 24
# assert factorial_iterative_while(6) == 720
# assert factorial_iterative_while(1) == 1
# assert factorial_iterative_while(0) == 1
# assert factorial_iterative_while(-7) == 1
# assert factorial_iterative_while(50) == 30414093201713378043612608166064768844377641568960512000000000000


def factorial(n,count):
    if count <= 1:
        return
    print(n)
    factorial(n*(n-1),count-1)


print(factorial(5,5))