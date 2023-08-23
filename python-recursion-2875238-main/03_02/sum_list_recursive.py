"""
Python Recursion Video Course
Robin Andrews - https://compucademy.net/
"""

listExample = [1,2,3,4]
def list_sum(a_list):
    sum = 0
    for i in a_list:
        sum+=i
    return sum



def list_sum_recursive(a_list):
    if not a_list:
        return 0
    else:
        return a_list[0] + list_sum(a_list[1:])


assert list_sum([2, 3, 5, 7]) == 17
assert list_sum([-4, -3, -2, -1, 10]) == 0

assert list_sum_recursive([2, 3, 5, 7]) == 17
assert list_sum_recursive([-4, -3, -2, -1, 10]) == 0
assert list_sum_recursive([]) == 0
assert list_sum_recursive([3]) == 3
assert list_sum_recursive([-5, -3]) == -8

# print(list_sum_recursive([1, 2, 3]))


