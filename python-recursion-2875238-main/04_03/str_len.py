"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""


def iterative_str_len(a_str):
    count = 0
    for i in a_str:
        count+=1
    return count


def recursive_str_len(a_str):
    if not a_str:
        return 0
    return recursive_str_len(a_str[1:]) + 1


input_str = "I love recursion"
print(len(input_str))  # Standard Pythonic way
print(iterative_str_len(input_str))
print(recursive_str_len(input_str))
