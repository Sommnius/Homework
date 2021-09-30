# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.
import math


def foo(some_list):
    product = math.prod(some_list)  # or use for-loop or lambda or...
    return list(product // c for c in some_list)


print(foo([1, 2, 3, 4, 5]))
