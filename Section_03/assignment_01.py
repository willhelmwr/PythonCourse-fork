# Assignment 1:
"""
    Create a function named merge_lists that accepts 2 lists.
    The function is supposed to merge both of those lists together
    and return the result.
"""

# your code below:

list_a = [1, 3, 5, 7, 9]
list_b = [2, 4, 6, 8, 0]

def merge_lists(a,  b):
    return sorted(a + b)

print(merge_lists(list_a, list_b))






































# solution Below:

# def merge_lists(list_a, list_b):
#     return list_a + list_b
#
# my_list = merge_lists([1,2,3],['a', 'b', 'c'])
# print(my_list)